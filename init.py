
class InitParser(object):
    def __init__(self):

        self.do_you_wanna_train = True                                                # 'Training will start'
        self.do_you_wanna_load_weights = True                  # 'Load weights'
        self.do_you_wanna_check_accuracy = False                                      # 'Model will be tested after the training or only this is done'

        # gpu setting
        self.multi_gpu = True                                                     # 'Decide to use one or more GPUs'
        self.gpu_id = '0,2,3'                                                          # 'Select the GPUs for training and testing'
        # optimizer setting
        self.lr = 0.001                                                          # 'Learning rate'
        self.weight_decay = 5e-4                                                      # 'Weight decay'
        # train setting
        self.increase_factor_data = 2                                                # 'Increase the data number passed each epoch'
        self.resample = True                                                      # 'Decide or not to rescale the images to a new resolution'
        self.new_resolution = (4, 4, 4)   # 2.5 before                          # 'New resolution'
        self.patch_size = [128, 128, 32]                                              # "Input dimension for the Unet3D"
        self.drop_ratio = 0                                                           # "Probability to drop a cropped area if the label is empty. All empty patches will be dropped for 0 and accept all cropped patches if set to 1"
        self.min_pixel = 0.2                                                         # "Percentage of minimum non-zero pixels in the cropped label"
        self.batch_size = 12                                                          # 'Batch size: the greater more GPUs are used and faster is the training'
        self.num_epoch = 300                                                         # "Number of epochs"
        self.init_epoch = 1
        self.stride_inplane = 32                                                      # "Stride size in 2D plane"
        self.stride_layer = 16                                                        # "Stride size in z direction"

        # path setting
        self.data_path = './dataset4/trainset/'                           # Training data folder
        self.test_path = './dataset4/testset/'                            # Testing data folder
        self.history_dir = './Historyvnet4'
        self.load_path = "/data5/hongyang/tunan/code_vesselseg/Historyvnet4/Checkpoint/Best_Dice.pth.gz"
        self.output_path = "./Historyvnet4/"

