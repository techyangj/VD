import os
import shutil
from torchvision import datasets, transforms

# 定义数据转换
transform = transforms.Compose([
    transforms.ToTensor()  # 将图像转换为 PyTorch Tensor
])

# 下载并加载 CIFAR-10 数据集
train_dataset = datasets.CIFAR10(root='../dataset', train=True, download=True, transform=transform)
test_dataset = datasets.CIFAR10(root='../dataset', train=False, download=True, transform=transform)


# 创建存储图片的目录
def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


# 保存图片到对应文件夹
def save_dataset(dataset, dataset_type='train'):
    root_dir = f'../dataset/cifar/{dataset_type}'
    create_dir(root_dir)

    # 获取类别名称
    classes = dataset.classes

    # 在根目录下为每个类别创建子文件夹
    for class_name in classes:
        class_dir = os.path.join(root_dir, class_name)
        create_dir(class_dir)

    # 遍历数据集，保存每张图片
    for i, (img, label) in enumerate(dataset):
        class_name = classes[label]
        class_dir = os.path.join(root_dir, class_name)

        # 将图像从 Tensor 转换为 PIL 格式
        img_pil = transforms.ToPILImage()(img)

        # 保存图像到对应的类别文件夹，文件名以序号命名
        img_path = os.path.join(class_dir, f'{i}.png')
        img_pil.save(img_path)

    print(f'{dataset_type} 数据集保存完成！')


# 保存训练集
save_dataset(train_dataset, dataset_type='train')

# 保存测试集
save_dataset(test_dataset, dataset_type='test')
