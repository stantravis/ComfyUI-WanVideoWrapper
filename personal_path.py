import os
import folder_paths

_BASE_PATH_ = r'd:\NN\Wan'  # <<<<<<< personal setup
if not os.path.exists(_BASE_PATH_): _BASE_PATH_ = None

MODEL_WV = {
    'Text-2-V 14B f8':'Wan2_1-T2V-14B_fp8_e4m3fn.safetensors',
    'Text-2-V 14B bf16':'wan2.1_t2v_14B_bf16.safetensors',
    'Img-2-V 14B 720p f8':'Wan2_1-I2V-14B-720P_fp8_e4m3fn.safetensors',
    'Img-2-V 14B 480p f8':'Wan2_1-I2V-14B-480P_fp8_e4m3fn.safetensors',
    'Text-2-V 1.3B f32':'1_3B/diffusion_pytorch_model.safetensors',
    }

LORAS_MV = None

VAE_WV = {
    'Wan2.1 VAE f32':'Wan2.1_VAE.pth',
    }

TE_WV = {
    'UMT5-xxl bf16':'models_t5_umt5-xxl-enc-bf16.pth',
    'clip VH14 f16':'open-clip-xlm-roberta-large-vit-huge-14_fp16.safetensors',
    'clip VH14 visual f32':'open-clip-xlm-roberta-large-vit-huge-14_visual_fp32.safetensors',
    }

CMF_REMAP = {
    "diffusion_models":MODEL_WV,
    "loras":LORAS_MV,
    "vae":VAE_WV,
    "text_encoders":TE_WV,

}

get_filename_list = folder_paths.get_filename_list

def get_filename_list_(cmf_dir):
    MODEL = CMF_REMAP.get(cmf_dir)
    #if MODEL is None: print ('*** CMF_REMAP None for',cmf_dir)
    if not _BASE_PATH_ or MODEL is None:
        return get_filename_list(cmf_dir)
    return list(MODEL.keys())

folder_paths.get_filename_list = get_filename_list_


get_full_path_or_raise = folder_paths.get_full_path_or_raise

def get_full_path_or_raise_(cmf_dir,model):
    MODEL = CMF_REMAP.get(cmf_dir)
    if not _BASE_PATH_ or MODEL is None:
        return get_full_path_or_raise(cmf_dir, model)
    return os.path.join(_BASE_PATH_,MODEL[model])

folder_paths.get_full_path_or_raise = get_full_path_or_raise_


get_full_path = folder_paths.get_full_path

def get_full_path_(cmf_dir,model):
    MODEL = CMF_REMAP.get(cmf_dir)
    if not _BASE_PATH_ or MODEL is None:
        return get_full_path(cmf_dir, model)
    return os.path.join(_BASE_PATH_,MODEL[model])

folder_paths.get_full_path = get_full_path_
