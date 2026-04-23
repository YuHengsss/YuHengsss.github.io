---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am a Ph.D. student at the [University of Sydney](https://www.sydney.edu.au/), supervised by [A/Prof. Chang Xu](https://changxu.xyz/). Before joining USYD, I spent one year at the [City University of Hong Kong](https://www.cityu.edu.hk/) as a Research Assistant under the supervision of [A/Prof. Minjing Dong](https://www.cs.cityu.edu.hk/~minjdong/). I received my Master's degree from [Tianjin University](http://www.tju.edu.cn/english/index.htm), where I was advised by [Prof. Xiaojie Guo](https://sites.google.com/view/xjguo), and my Bachelor's degree from [Central South University](https://en.csu.edu.cn/).

My research focuses on **efficient and generalizable visual perception**. I am particularly interested in:

- **Multimodal Large Language Models (MLLMs)**, with an emphasis on fine-grained perception and efficient vision-language-action models.
- **State Space Models** (e.g., Mamba) for vision.
- **Vision Foundation Models**, including training-free open-vocabulary segmentation.
- **Object detection** in images and videos.

I have published at top-tier venues including ICLR, ICCV, NeurIPS, AAAI, and IJCV. See my <a href='https://scholar.google.com/citations?user=sn2PeEkAAAAJ'>Google Scholar</a> <a href='https://scholar.google.com/citations?user=sn2PeEkAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a> for the full list.


# 🔥 News
- *2026.04*: &nbsp;📄 New preprint "Q-Zoom: Query-Aware Adaptive Perception for Efficient Multimodal Large Language Models" is on [arXiv](https://arxiv.org/abs/2604.06912).
- *2026.01*: &nbsp;🎉 Two papers accepted to **ICLR 2026**!
- *2026.01*: &nbsp;🎉 Our paper on practical video object detection is accepted by **IJCV 2026**.
- *2025.09*: &nbsp;I started my PhD at the University of Sydney.
- *2025.07*: &nbsp;🎉 Two papers accepted to **ICCV 2025**.
- *2025.05*: &nbsp;🎖 Awarded the Faculty of Engineering Research Support Scholarship, USYD.
- *2024.09*: &nbsp;🎉 "Multi-Scale VMamba" accepted to **NeurIPS 2024**.

# 📝 Publications

<sup>†</sup> denotes equal contribution.

- [Catching the Details: Self-Distilled RoI Predictors for Fine-Grained MLLM Perception](https://arxiv.org/abs/2509.16944). **Yuheng Shi**, Xiaohuan Pei, Minjing Dong, Chang Xu. *ICLR*, 2026. [\[Code\]](https://github.com/YuHengsss/SD-RPN)
- [Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation](https://arxiv.org/abs/2509.22093). Xiaohuan Pei, Yuxing Chen, **Yuheng Shi**, Siyu Xu, Yunke Wang, Chang Xu. *ICLR*, 2026.
- [Practical Video Object Detection via Feature Selection and Aggregation](https://arxiv.org/abs/2407.19650). **Yuheng Shi**<sup>†</sup>, Tong Zhang<sup>†</sup>, Xiaojie Guo. *IJCV*, 2026. [\[Code\]](https://github.com/YuHengsss/YOLOV)
- [VSSD: Vision Mamba with Non-Causal State Space Duality](https://openaccess.thecvf.com/content/ICCV2025/html/Shi_VSSD_Vision_Mamba_with_Non-Causal_State_Space_Duality_ICCV_2025_paper.html). **Yuheng Shi**, Minjing Dong, Mingjia Li, Chang Xu. *ICCV*, 2025. [\[Code\]](https://github.com/YuHengsss/VSSD)
- [Harnessing Vision Foundation Models for High-Performance, Training-Free Open Vocabulary Segmentation](https://openaccess.thecvf.com/content/ICCV2025/html/Shi_Harnessing_Vision_Foundation_Models_for_High-Performance_Training-Free_Open_Vocabulary_Segmentation_ICCV_2025_paper.html). **Yuheng Shi**, Minjing Dong, Chang Xu. *ICCV*, 2025. [\[Code\]](https://github.com/YuHengsss/Trident)
- [Multi-Scale VMamba: Hierarchy in Hierarchy Visual State Space Model](https://proceedings.neurips.cc/paper_files/paper/2024/hash/2d69e771d9f274f7c624198ea74f5b98-Abstract-Conference.html). **Yuheng Shi**, Minjing Dong, Chang Xu. *NeurIPS*, 2024. [\[Code\]](https://github.com/YuHengsss/MSVMamba)
- [YOLOV: Making Still Image Object Detectors Great at Video Object Detection](https://ojs.aaai.org/index.php/AAAI/article/view/25320). **Yuheng Shi**, Naiyan Wang, Xiaojie Guo. *AAAI*, 2023. [\[Code\]](https://github.com/YuHengsss/YOLOV)

# 📄 Preprints
- [Q-Zoom: Query-Aware Adaptive Perception for Efficient Multimodal Large Language Models](https://arxiv.org/abs/2604.06912). **Yuheng Shi**, Xiaohuan Pei, Linfeng Wen, Minjing Dong, Chang Xu. *arXiv:2604.06912*, 2026. [\[Code\]](https://github.com/YuHengsss/Q-Zoom)
- [TSTTC: A Large-Scale Dataset for Time-to-Contact Estimation in Driving Scenarios](https://arxiv.org/abs/2309.01539). **Yuheng Shi**, Zehao Huang, Yan Yan, Naiyan Wang, Xiaojie Guo. *arXiv:2309.01539*, 2023.

# 🎖 Honors and Awards
- *2025*, Faculty of Engineering Research Support Scholarship, University of Sydney.
- *2023*, 2nd Place, ICCV 2023 VCL Challenge: Robust Raw Object Detection.
- *2021*, Outstanding Graduate, Central South University.
- *2018 – 2020*, Second Class Scholarship, Central South University.

# 📖 Educations
- *2025.09 – Now*, Ph.D. in Computer Science, University of Sydney. Supervisor: A/Prof. Chang Xu.
- *2021.09 – 2024.06*, M.Sc. in Computer Science and Technology, Tianjin University. Supervisor: Prof. Xiaojie Guo.
- *2017.09 – 2021.06*, B.Eng. in Intelligence Science and Technology, Central South University.

# 💼 Work Experience
- *2024 – 2025*, Research Assistant, City University of Hong Kong. Supervised by A/Prof. Minjing Dong and A/Prof. Chang Xu.
- *2022 – 2023*, Research Intern, TuSimple. Supervised by Naiyan Wang and Zehao Huang.

# 🛎 Academic Services
- **Conference Reviewer**: NeurIPS, ICLR, ICML, ICCV.
- **Journal Reviewer**: T-PAMI, TMLR.
