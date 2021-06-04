# GLSD: The Global Large-Scale Ship Database and Baseline Evaluations

Table 1. Comparison among GLSD and object detection datasets. 
|Dataset|main categories|instances|images|image size|
|:---:|:---:|:---:|:---:|:---:|
|VOC2007|1|791|363|random|
|CIFAR-10|1|6,000|6,000|32 × 43|
|Caitech-256|4|418|418|random|
|ImageNet|1|525|613|random|
|[SeaShips](http://www.lmars.whu.edu.cn/prof_web/shaozhenfeng/datasets/SeaShips(7000).zip) (first large-scale ship database)|6|40,077|31,455|1,920 × 1,080|
|GLSD|13|152,776|212,357|random|

Table 2. The definition of categories in GLSD. 
|Categories|Definition|
|:---:|:---:|
|Ore carrier | Ships with small stowage factors|
|Bulk cargo carrier | Ships with large stowage factors |
|General cargo ship | Ships that transporting machinery, equipment, building materials, daily necessities, etc. |
|Container ship | Ships that specialize in the transport of containerized goods |
|Fishing boat | Ships for catching and harvesting aquatic animals and plants |
|Passenger ship | Vessels used to transport passengers or pedestrians |
|Sailing boat | Boats propelled partly or entirely by sails |
|Barge | Ships for cargo transportation between inland ports |
|War ship | Naval ships that are built and primarily intended for naval warfare |
|Oil carrier | Ships designed for the bulk transport of oil or its products|
|Tug | Tug maneuvers other vessels by pushing or pulling them either by direct contact or by means of a tow line|
|Canoe | Lightweight narrow vessel, typically pointed at both ends and open on top |
|Speed boat | Small boats with a powerful engine that travels very fast  |

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
