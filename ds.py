{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP4cE71ElzshMTS0jdQqbeo",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/t200056/stream/blob/main/ds.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "E6d2bPHdq_c9"
      },
      "outputs": [],
      "source": [
        "import streamlit as st\n",
        "\n",
        "#  기계학습 모델 파일 로드(모델명 : _______)\n",
        "import joblib\n",
        "model = joblib.load('logistic_regression_model.pkl')\n",
        "\n",
        "# 만든 모델로 테스트 데이터에 대해 예측하기\n",
        "st.title('합불 분류 지능에이전트')\n",
        "\n",
        "col1, col2 = st.columns(2)\n",
        "\n",
        "with col1:\n",
        "      st.subheader(' 1. 기계학습 모델 제작과정 ')\n",
        "      st.write(' - 기계학습 알고리즘 : 로지스틱 회귀 ')\n",
        "      st.write(' - 학습 데이터 출처 : https://www.kaggle.com/')\n",
        "      st.write(' - 총 데이터 건 수: 30건')\n",
        "      st.write(' - 훈련    데이터 : 21건')\n",
        "      st.write(' - 테스트 데이터 : 9건')\n",
        "with col2:\n",
        "      st.subheader('2. 기계학습 모델 평가')\n",
        "      image_path = '/content/chart.png' # 로컬 이미지 파일 경로\n",
        "      st.image(image_path )   # 이미지 불러오기\n",
        "\n",
        "st.subheader('3. 지능 에이전트 활용 방법 ')\n",
        "st.write('**** 공부시간을 입력하세요.. 인공지능이 당신의 합격/불합격 분류 결과를 알려드립니다!')\n",
        "\n",
        "# 사용자 입력\n",
        "a = st.number_input(\"공부시간\", min_value=0)\n",
        "\n",
        "# 예측 버튼 만들기\n",
        "if st.button(\"인공지능의 분류 결과\"):\n",
        "        input_data = [[a]]\n",
        "        p = model.predict(input_data)\n",
        "         # 단순 조건문으로 예측 결과 출력\n",
        "        if p[0] == 1:\n",
        "              st.success('인공지능 분류 결과는 합격입니다........... 그러나, 방심은 금물입니다!')\n",
        "        else:\n",
        "              st.success('인공지능 분류 결과는 불합격입니다.......... 더 열심히 공부하면 됩니다!')"
      ]
    }
  ]
}