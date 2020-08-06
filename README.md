# GLSD: The Global Large-Scale Ship Database and Baseline Evaluations


Table 1. Comparison among GLSD and object detection datasets. 
|Dataset|main categories|instances|images|image size|
|:---:|:---:|:---:|:---:|:---:|
|VOC2007|1|791|363|random|
|CIFAR-10|1|6000|6000|32 × 43|
|Caitech-256|4|418|418|random|
|ImageNet|1|525|613|random|
|[SeaShips](http://www.lmars.whu.edu.cn/prof_web/shaozhenfeng/datasets/SeaShips(7000).zip) (first large-scale ship database)|6|40077|31455|1,920 × 1,080|
|GLSD|10|-|-|random|

Table 2. The definition of categories in GLSD. 
|Categories|Definition|
|:---:|:---:|
|ore carrier | Ships with small stowage factors |
|bulk cargo carrier | Ships with large stowage factors |
|general cargo ship | Ships transporting machinery, equipment, building materials, daily necessities, etc. |
|container ship | Ships specializing in the transport of containerized goods |
|fishing boat | Ships for catching and harvesting aquatic animals and plants |
|passenger ship | Vessels used to transport passengers or pedestrians, including passenger ships, yachts |
|sailing boat | sailing boat |
|barge | Suitable for cargo transportation between inland ports |
|warship | warship|
|oil carrier | oil carrier |

See more details of [ports information](https://github.com/jiaming-wang/GLSD/blob/master/Ports%20list.md) in GLSD.

If you find this work useful, please consider citing it.
```
@article{shao2018seaships,
	title={Seaships: A large-scale precisely annotated dataset for ship detection},
	author={Shao, Zhenfeng and Wu, Wenjing and Wang, Zhongyuan and Du, Wan and Li, Chengyuan},
	journal={IEEE Transactions on Multimedia},
	volume={20},
	number={10},
	pages={2593--2604},
	year={2018}
}
```
