{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Day29",
      "provenance": [],
      "authorship_tag": "ABX9TyNgr1XCbEWUKCrc0IwxIvEd",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/BrewTC/Python60Days/blob/main/Day29.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Dod8utuzELkM",
        "outputId": "1439f7b2-177d-4456-df97-eefc499bd03b"
      },
      "source": [
        "# library\n",
        "import matplotlib.pyplot as plt\n",
        "import numpy as np\n",
        "import pandas as pd\n",
        "from scipy import stats\n",
        "import math\n",
        "import statistics\n",
        "import seaborn as sns\n",
        "\n",
        "# 輸入資料\n",
        "boys=[164, 176, 169, 169, 165, 175, 159, 151, 144, 160, 183, 165, 156, 170,\n",
        " 164, 173, 165, 163, 177, 171]\n",
        "\n",
        "# 計算統計量_平均數的方法\n",
        "mean_boy=np.mean(boys)\n",
        "print(\"男孩身高平均=\",mean_boy)\n",
        "\n",
        "statistics_mean_boy=statistics.mean(boys)\n",
        "print(\"statistics_mean_boy=\",statistics_mean_boy)"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "男孩身高平均= 165.95\n",
            "statistics_mean_boy= 165.95\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0ItqZZw34t_r",
        "outputId": "b8629b92-b84f-4382-e48b-088c9ccc7254"
      },
      "source": [
        "# 計算統計量_中位數的方法\n",
        "np_median_boy=np.median(boys,axis=None)\n",
        "print(\"np_median_boy=\",np_median_boy)\n",
        "\n",
        "statistics_median_boy=statistics.median(boys)\n",
        "print(\"statistics_median_boy=\",statistics_median_boy)"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "np_median_boy= 165.0\n",
            "statistics_median_boy= 165.0\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UUJZX2LB47oO",
        "outputId": "0386434d-d1d7-4ffd-ec23-60d797095dc0"
      },
      "source": [
        "# 統計量_眾數\n",
        "# 統計量的眾數，如果有多個眾數，取最小的值當眾數。\n",
        "mode_boy=stats.mode(boys,axis=None)\n",
        "print(\"男孩身高眾數=\",mode_boy)\n",
        "print(\"男孩身高眾數=\",mode_boy[0][0])\n",
        "\n",
        "\n",
        "# 統計量_眾數\n",
        "statistics_mode_boy=statistics.mode(boys)\n",
        "print(\"statistics_mode_boy=\",statistics_mode_boy)"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "男孩身高眾數= ModeResult(mode=array([165]), count=array([3]))\n",
            "男孩身高眾數= 165\n",
            "statistics_mode_boy= 165\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0TxugkAF5A8H",
        "outputId": "77986b92-82b7-489d-dfbd-d26efc9b42c3"
      },
      "source": [
        "#全距\n",
        "#rangeV=max(boys)-min(boys)\n",
        "def rangeV(x): \n",
        "  return(max(x)-min(x))\n",
        "    \n",
        "print(rangeV(boys))"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "39\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XJlBcJWE5E4J",
        "outputId": "25050f25-9116-4b0e-ebfc-060a86db6045"
      },
      "source": [
        "# 計算變異數的方法\n",
        "print(\"男孩身高變異數=\",statistics.variance(boys))\n",
        "print(\"男孩身高變異數=\",np.var(boys,ddof=1))"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "男孩身高變異數= 84.89210526315789\n",
            "男孩身高變異數= 84.89210526315789\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CtQmm3bE5KPU",
        "outputId": "8f4e29ba-04bb-4a30-8945-b4ac9890e14a"
      },
      "source": [
        "# 統計量_標準差的方法\n",
        "# 樣本標準差\n",
        "#ddof=1, 回傳 sample standard deviation 樣本標準差，分母(n-1)，無偏估計\n",
        "std_boy=np.std(boys,ddof=1)\n",
        "print(\"男孩身高標準差=\",std_boy)\n",
        "\n",
        "statistics_stdev_boy=statistics.stdev(boys)\n",
        "print(\"statistics_mean_boy=\",statistics_stdev_boy)"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "男孩身高標準差= 9.213691185575838\n",
            "statistics_mean_boy= 9.213691185575838\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8JVyr8Pl5Rgp",
        "outputId": "8258ae10-35c2-4da7-cb23-270cc4b1e7f8"
      },
      "source": [
        "# python 百分位數\n",
        "# np\n",
        "print(\"90百分位數=\",np.percentile(boys, 90))\n",
        "print(\"50百分位數=\",np.percentile(boys, 50))\n",
        "print(\"20百分位數=\",np.percentile(boys, 20))\n",
        "#stat\n",
        "print(\"20百分位數=\",stats.scoreatpercentile(boys, 20))"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "90百分位數= 176.1\n",
            "50百分位數= 165.0\n",
            "20百分位數= 159.8\n",
            "20百分位數= 159.8\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CiBZXEY05abf",
        "outputId": "331522b1-f984-4b80-d1af-67a2d05e3725"
      },
      "source": [
        "#計算峰度和偏度\n",
        "print(stats.skew(boys))\n",
        "print(stats.kurtosis(boys))"
      ],
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "-0.47132127317376954\n",
            "0.19395882957876331\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 281
        },
        "id": "zEllXAcV5kVn",
        "outputId": "f2c490e7-9f1d-4d82-88b6-ab048021e74e"
      },
      "source": [
        "# pandas和 stat 接近\n",
        "# python的峰帶\n",
        "\n",
        "#最後，畫圖看分布\n",
        "plt.hist(boys,alpha=.4,bins=40)\n",
        "plt.title('boy,skewness={0},kurtosis={1}'.format(round(stats.skew(boys),2),round(stats.kurtosis(boys),2)))\n",
        "plt.axvline(x=mean_boy)\n",
        "plt.show()"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "gNa4o4hO5tT2"
      },
      "source": [
        "# 今天學到不同統計量之間特性，\n",
        "# 試著分析男生女生身高資料，\n",
        "# 試著回答下面的問題:\n",
        "# Q1:試著用今天所教的內容，如何描述這兩組資料的樣態?\n",
        "# Q2: 請問男生和女生在平均身高上誰比較高?\n",
        "# Q3:請問第二題的答案和日常生活中觀察的一致嗎? 如果不一致，你覺得原因可能為何?\n"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}