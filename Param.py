import os
from torchvision import datasets, transforms


dataset = "mnist"


t_lst = [
    "10101010",  # 客户端1的触发器
    "11111111",  # 客户端2的触发器
    "01010101",  # 客户端3的触发器
    # 假设有更多客户端
]
poisonRate = 0.5

channel_count = 1 # mnist 1  cifar gtsrb 3
# Initialize missing variables
class_num = 10       # 个数
num_samples_poi = 500   # 毒化个数
init_lr = 0.001         # 初始学习率
joint_init_lr = 0.001   # 联合学习 初始学习率
epoch = 50               # epoch的个数
joint_epoch = 50        # 联合学习的epoch个数
batch_size = 64         # batch_size
total_classes = 10      # 总共的class
num_classes = 2
clientNum = 3           # 客户端个数
clients = ["client1", "client2", "client3"] # 客户端
model_batch = 64        #
testDataNum = list(range(1, 101))    # 迭代
delClass = [0, 1]
delClassNum = 2
# Dynamic epoch and learning rate functions
def num_epoch(s):
    return 50  # or implement dynamic logic

def lr(s):
    return 0.001  # or implement dynamic logic


def clean_test(test_data):
    # 定义预处理，包括调整图像大小
    transform = transforms.Compose([
        transforms.Resize((28, 28)),  # 调整图像大小为224x224
        transforms.ToTensor(),  # 将图像转换为Tensor
    ])

    # 创建新的数据集，应用transform
    transformed_test_data = [(transform(image), label) for image, label in test_data]

    return transformed_test_data



# 定义 outfile_train 函数，生成输出文件路径
def outfile_train(model_type):
    """
    生成输出文件路径，用于存储模型的训练日志或结果
    :param model_type: 模型类型（例如 'incremental' 或 'joint'）
    :return: 输出文件的路径字符串
    """
    base_output_dir = "./model_logs"  # 基础目录，用于存放日志文件
    os.makedirs(base_output_dir, exist_ok=True)  # 如果目录不存在，则创建目录
    log_filename = f"{model_type}_training_log.txt"  # 根据模型类型命名日志文件
    return os.path.join(base_output_dir, log_filename)  # 返回完整的文件路径

def num_samples(s):
    return 100  # 每次从 clean_data 中抽取 100 个样本