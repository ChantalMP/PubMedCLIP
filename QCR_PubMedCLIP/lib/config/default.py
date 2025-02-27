from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


from yacs.config import CfgNode as CN


_C = CN()

# ----- BASIC SETTINGS -----
_C.NAME = "default"
_C.OUTPUT_DIR = "/home/VQAMed/output"
_C.PIN_MEMORY = True
_C.COLOR_SPACE = "RGB"
_C.RESUME_MODEL = ""
_C.RESUME_MODE = "all"
_C.CPU_MODE = False
_C.EVAL_MODE = False
_C.SEED = 5


# ----- DATASET BUILDER -----
_C.DATASET = CN()
_C.DATASET.DATASET = "MED"
_C.DATASET.DATA_DIR = ""
_C.DATASET.DATA_TYPE = "jpg"
_C.DATASET.TRAIN_CSV = ""
_C.DATASET.VALID_CSV = ""
_C.DATASET.TRAIN_JSON = ""
_C.DATASET.VALID_JSON = ""
_C.DATASET.IMBALANCECIFAR = CN()
_C.DATASET.IMBALANCECIFAR.RATIO = 0.01
_C.DATASET.IMBALANCECIFAR.RANDOM_SEED = 0


# ----- CLASSIFIER BUILDER -----
_C.CLASSIFIER = CN()
_C.CLASSIFIER.TYPE = "FC"
_C.CLASSIFIER.BIAS = True


# ----- LOSS BUILDER -----
_C.LOSS = CN()
_C.LOSS.LOSS_TYPE = "CrossEntropy"

_C.LOSS.CSCE = CN()
_C.LOSS.CSCE.SCHEDULER = "default"
_C.LOSS.CSCE.DRW_EPOCH = 160

# _C.LOSS.LDAM= CN()
# _C.LOSS.LDAM.DRW_EPOCH = 160
# _C.LOSS.LDAM.MAX_MARGIN = 0.5

# ----- TRAIN BUILDER -----
_C.TRAIN = CN()
_C.TRAIN.BATCH_SIZE = 32
_C.TRAIN.N_EPOCH = 60
_C.TRAIN.SHUFFLE = True
_C.TRAIN.NUM_WORKERS = 8
_C.TRAIN.RESUME = False
_C.TRAIN.INPUT_SNAPSHOT = ""
# _C.TRAIN.TENSORBOARD = CN()
# _C.TRAIN.TENSORBOARD.ENABLE = True

# ----- COMBINER -----
_C.TRAIN.COMBINER = CN()
_C.TRAIN.COMBINER.TYPE = "default"

# ----- SAMPLER -----
_C.TRAIN.SAMPLER = CN()
_C.TRAIN.SAMPLER.TYPE = "default"

_C.TRAIN.SAMPLER.DUAL_SAMPLER = CN()
_C.TRAIN.SAMPLER.DUAL_SAMPLER.ENABLE = False
_C.TRAIN.SAMPLER.DUAL_SAMPLER.TYPE = "reversed"

_C.TRAIN.SAMPLER.WEIGHTED_SAMPLER = CN()
_C.TRAIN.SAMPLER.WEIGHTED_SAMPLER.TYPE = "balance"

# ----- OPTIMIZER -----
_C.TRAIN.OPTIMIZER = CN()
_C.TRAIN.OPTIMIZER.TYPE = "SGD"
_C.TRAIN.OPTIMIZER.BASE_LR = 0.1
_C.TRAIN.OPTIMIZER.MOMENTUM_CNN = 0.9
_C.TRAIN.OPTIMIZER.EPS_CNN = 0.9
_C.TRAIN.OPTIMIZER.WEIGHT_DECAY = 4e-4


_C.TRAIN.LR_SCHEDULER = CN()
_C.TRAIN.LR_SCHEDULER.TYPE = "multistep"
_C.TRAIN.LR_SCHEDULER.LR_STEP = [40, 50]
_C.TRAIN.LR_SCHEDULER.LR_FACTOR = 0.1
_C.TRAIN.LR_SCHEDULER.WARM_EPOCH = 5
_C.TRAIN.LR_SCHEDULER.COSINE_DECAY_END = 0


# ----- ACTIVATION/DROPOUT -----
_C.TRAIN.ACTIVATION = 'relu'
_C.TRAIN.DROPOUT = 0.5


# ----- ATTENTION -----
_C.TRAIN.ATTENTION = CN()
_C.TRAIN.ATTENTION.MODE = "BAN"
_C.TRAIN.ATTENTION.GLIMPSE = 2
_C.TRAIN.ATTENTION.USE_COUNTER = False
_C.TRAIN.ATTENTION.NUM_STACKS = 2


# ----- QUESTION -----
_C.TRAIN.QUESTION = CN()
_C.TRAIN.QUESTION.CLIP = False
_C.TRAIN.QUESTION.BERT = False
#_C.TRAIN.QUESTION.BERT_MODEL = "emilyalsentzer/Bio_ClinicalBERT"
_C.TRAIN.QUESTION.BERT_MODEL = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
_C.TRAIN.QUESTION.RNN = 'GRU'
_C.TRAIN.QUESTION.LENGTH = 12
_C.TRAIN.QUESTION.TFIDF = False
_C.TRAIN.QUESTION.USEDATA = True 
_C.TRAIN.QUESTION.CAT = True
_C.TRAIN.QUESTION.HID_DIM = 10
_C.TRAIN.QUESTION.CLS_HID_DIM = 1024
_C.TRAIN.QUESTION.QTYPE_ATTENTION = "visual_multiply"


# ----- VISION -----
_C.TRAIN.VISION = CN()
_C.TRAIN.VISION.V_DIM = 64
_C.TRAIN.VISION.AUTOENCODER = False 
_C.TRAIN.VISION.AE_PATH = ""
_C.TRAIN.VISION.AE_ALPHA = 0.001
_C.TRAIN.VISION.MAML = False
_C.TRAIN.VISION.MAML_PATH = ""
_C.TRAIN.VISION.CLIP = False
_C.TRAIN.VISION.CLIP_ORG = False
_C.TRAIN.VISION.CLIP_PATH = ""
_C.TRAIN.VISION.CLIP_Q_PATH = ""
_C.TRAIN.VISION.CLIP_VISION_ENCODER = "ViT-B/32"
_C.TRAIN.VISION.OTHER_MODEL = False

# ----- CLASSIFIER -----
_C.TRAIN.CLASSIFIER = CN()
_C.TRAIN.CLASSIFIER.BBN = False


# testing
_C.TEST = CN()
_C.TEST.BATCH_SIZE = 32
_C.TEST.NUM_WORKERS = 8
_C.TEST.MODEL_FILE = ""
_C.TEST.RESULT_DIR = "test_results"

_C.TRANSFORMS = CN()
_C.TRANSFORMS.TRAIN_TRANSFORMS = ("random_resized_crop", "random_horizontal_flip")
_C.TRANSFORMS.TEST_TRANSFORMS = ("shorter_resize_for_crop", "center_crop")

_C.TRANSFORMS.PROCESS_DETAIL = CN()
_C.TRANSFORMS.PROCESS_DETAIL.RANDOM_CROP = CN()
_C.TRANSFORMS.PROCESS_DETAIL.RANDOM_CROP.PADDING = 4
_C.TRANSFORMS.PROCESS_DETAIL.RANDOM_RESIZED_CROP = CN()
_C.TRANSFORMS.PROCESS_DETAIL.RANDOM_RESIZED_CROP.SCALE = (0.08, 1.0)
_C.TRANSFORMS.PROCESS_DETAIL.RANDOM_RESIZED_CROP.RATIO = (0.75, 1.333333333)


def update_config(cfg, args):
    cfg.defrost()
    cfg.merge_from_file(args.cfg)

    cfg.freeze()
