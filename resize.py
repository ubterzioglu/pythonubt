import os
import shutil
import subprocess
from pathlib import Path
from PIL import Image
from tqdm import tqdm

# ==== AYARLAR ====
REALESRGAN_EXE = r"C:\AI\realesrgan\realesrgan-ncnn-vulkan.exe"
MODELS_DIR     = r"C:\AI\realesrgan\models"

INPUT_DIR = r"C:\Users\ubter\OneDrive\Desktop\original_images"
OUTPUT_DIR = r"C:\Users\ubter\OneDrive\Desktop\upscaled_10x"
TEMP_DIR   = r"C:\Users\ubter\OneDrive\Desktop\.tmp_realesrgan"

# GPU seçimi: 0 = Intel iGPU, 1 = NVIDIA RTX 3050 (önerilen), -1 = CPU
GPU  = "1"
# VRAM yetmezse düşür: 200 -> 100 -> 64
TILE = "200"

# Anime/video modellerini fallback olarak kullanmak ister misin?
USE_ANIME_FALLBACK = False  # True yaparsan x2plus yoksa animev3-x2 denenir

EXTS = {".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff", ".webp"}
Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(TEMP_DIR).mkdir(parents=True, exist_ok=True)

def has_model(name: str) -> bool:
    return (Path(MODELS_DIR, f"{name}.param").exists()
            and Path(MODELS_DIR, f"{name}.bin").exists())

HAS_X4PLUS   = has_model("realesrgan-x4plus")
HAS_X2PLUS   = has_model("realesrgan-x2plus")
HAS_AV3_X2   = has_model("realersr-animevideov3-x2")  # sende var
HAS_AV3_X3   = has_model("realersr-animevideov3-x3")
HAS_AV3_X4   = has_model("realersr-animevideov3-x4")

if not HAS_X4PLUS:
    missing = ["realesrgan-x4plus.param/bin (zorunlu)"]
    raise FileNotFoundError(
        f"Model eksik: {missing}\nLütfen {MODELS_DIR} içine yerleştir."
    )

def run_realesrgan(inp, out, scale, model):
    cmd = [
        REALESRGAN_EXE,
        "-i", inp,
        "-o", out,
        "-s", str(scale),
        "-n", model,
        "-t", TILE,
        "-g", GPU,
        "-m", MODELS_DIR
    ]
    subprocess.run(cmd, check=True)

def upscale_lanczos(src_path: Path, dst_path: Path, scale: float):
    with Image.open(src_path) as im:
        w, h = im.size
        target = (int(round(w * scale)), int(round(h * scale)))
        im_up = im.resize(target, Image.Resampling.LANCZOS)
        ext = dst_path.suffix.lower()
        if ext in [".jpg", ".jpeg"]:
            im_up = im_up.convert("RGB")
            im_up.save(dst_path, quality=95, subsampling=0)
        else:
            im_up.save(dst_path)

def upscale_chain_to_10x(image_path: Path, out_path: Path):
    """
    Tercihli zincir:
      1) x4plus -> 2) x2plus -> 3) 1.25× LANCZOS  (toplam 10×)
    x2plus yoksa:
      a) (varsayılan) x4plus -> 2.5× LANCZOS      (toplam 10×)
      b) (opsiyonel)  x4plus -> animev3-x2 -> 1.25× LANCZOS  (toplam 10×)
    """
    # 1) 4×
    tmp4 = Path(TEMP_DIR, f"{image_path.stem}_4x.png")
    run_realesrgan(str(image_path), str(tmp4), 4, "realesrgan-x4plus")

    if HAS_X2PLUS:
        # 2) 2× (8× olur)
        tmp8 = Path(TEMP_DIR, f"{image_path.stem}_8x.png")
        run_realesrgan(str(tmp4), str(tmp8), 2, "realesrgan-x2plus")
        # 3) 1.25× (10×)
        if out_path.suffix.lower() not in [".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff", ".bmp"]:
            out_path = out_path.with_suffix(".png")
        upscale_lanczos(tmp8, out_path, 1.25)
        tmp8.unlink(missing_ok=True)
    else:
        if USE_ANIME_FALLBACK and HAS_AV3_X2:
            # 2) animev3-x2 (8× olur)
            tmp8 = Path(TEMP_DIR, f"{image_path.stem}_8x.png")
            run_realesrgan(str(tmp4), str(tmp8), 2, "realersr-animevideov3-x2")
            # 3) 1.25×
            if out_path.suffix.lower() not in [".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff", ".bmp"]:
                out_path = out_path.with_suffix(".png")
            upscale_lanczos(tmp8, out_path, 1.25)
            tmp8.unlink(missing_ok=True)
        else:
            # Sade fallback: 4× -> 2.5× LANCZOS = 10×
            if out_path.suffix.lower() not in [".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff", ".bmp"]:
                out_path = out_path.with_suffix(".png")
            upscale_lanczos(tmp4, out_path, 2.5)

    tmp4.unlink(missing_ok=True)

def main():
    images = [p for p in Path(INPUT_DIR).iterdir() if p.is_file() and p.suffix.lower() in EXTS]
    if not images:
        print("Girdi klasöründe uygun resim bulunamadı.")
        return

    print(f"{len(images)} adet görsel bulundu. İşleniyor…")
    for p in tqdm(images):
        out = Path(OUTPUT_DIR) / p.name
        try:
            upscale_chain_to_10x(p, out)
        except subprocess.CalledProcessError as e:
            print(f"[HATA][{p.name}] Real-ESRGAN komutu başarısız: {e}")
        except Exception as e:
            print(f"[HATA][{p.name}] {e}")

    # Geçicileri temizle
    try:
        if Path(TEMP_DIR).exists() and not any(Path(TEMP_DIR).iterdir()):
            shutil.rmtree(TEMP_DIR, ignore_errors=True)
    except Exception:
        pass

    print("Bitti ✅")

if __name__ == "__main__":
    main()
