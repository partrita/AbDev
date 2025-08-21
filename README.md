# AbDev: 단일클론항체(mAb)의 생물리학적 특성 예측 모델링

AbDev는 단일클론항체(mAb)의 12가지 주요 생물리학적 특성 분석을 위해 설계된 포괄적인 예측 모델 패키지입니다. 이 도구는 딥러닝 기반 도구인 DeepSP와 머신러닝 기술을 결합하여 mAb의 가변 영역 서열을 기반으로 통찰력을 제공합니다.

-----

## 시작하기

AbDev를 효과적으로 활용하려면 아래에 설명된 가이드라인을 따르십시오:

### 특징 준비

1.  CSV 파일 준비: 먼저 이 가이드에서 제공하는 형식을 참조하여 `Sequence_Info.csv`라는 이름의 CSV 파일을 준비합니다. 이 파일에는 분석하고자 하는 mAb의 가변 영역 서열이 포함되어야 합니다.

### DeepSP로 공간적 특성 생성하기

2.  DeepSP 노트북 실행: `DeepSP.ipynb` 노트북 파일을 사용하여 저희 그룹이 개발한 딥러닝 기반 도구인 DeepSP를 실행합니다. DeepSP는 mAb의 서열을 기반으로 30가지 공간적 특성을 생성하도록 설계되었습니다.
      * 완료되면 추가 분석에 필요한 공간적 특성이 포함된 `SAPSCM.csv` 파일을 얻게 됩니다.

### AbDev로 생물리학적 특성 예측하기

3.  AbDev 노트북 실행: 다음으로 `AbDev.ipynb` 노트북 파일을 실행합니다. 이 단계는 이전 단계에서 생성된 특징들을 처리하여 `Prediction_Result.csv` 파일을 생성합니다. 이 파일에는 분석된 mAb의 12가지 생물리학적 특성에 대한 예측이 포함됩니다. 또는 `train.py`를 실행하여 결과를 직접 얻을 수도 있습니다.

-----

## 인용

  * 연구에 DeepSP를 사용할 경우 다음 논문을 인용해 주십시오.
    L. Kalejaye, I.E. Wu, T. Terry and P.K. Lai, DeepSP: Deep Learning-Based Spatial Properties to Predict Monoclonal Antibody Stability, *Comput. Struct. Biotechnol. J.*, 23:2220–2229, 2024.
    
  * 연구에 AbDev를 사용할 경우 다음 논문을 인용해 주십시오.
    I.E. Wu, L. Kalejaye and P.K. Lai, "Machine Learning Models for Predicting Monoclonal Antibody Biophysical Properties from Molecular Dynamics Simulations and Deep Learning-based Surface Descriptors", *Mol. Pharm*, 2024.
    