{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Day30.py",
      "provenance": [],
      "authorship_tag": "ABX9TyPaE9c3QZNeNS+vuAcvaxBQ",
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
        "<a href=\"https://colab.research.google.com/github/BrewTC/Python60Days/blob/main/Day30.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "dzWbclIgS1Z7"
      },
      "source": [
        "import matplotlib.pyplot as plt\n",
        "import numpy as np\n",
        "import pandas as pd\n",
        "from scipy import stats\n",
        "import math\n",
        "import statistics"
      ],
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 313
        },
        "id": "6VoH3U1TTDBI",
        "outputId": "19b6c02d-fe68-4146-d427-fa85a7549f50"
      },
      "source": [
        "'''\n",
        "# 離散均勻分配 (Discrete Uniform Distribution)\n",
        "# 前提：其中有限個數值擁有相同的機率。\n",
        "'''\n",
        "# 1.定義離散均勻分配的基本資訊\n",
        "\n",
        "low=1 \n",
        "high=7\n",
        "r = np.arange(low,high)\n",
        "# 2.計算離散均勻分配的概率質量分佈 (probability mass function)\n",
        "# 之所以稱為質量，是因為離散的點\n",
        "# 產生 x 軸的點\n",
        "#r = np.arange(stats.randint.ppf(0.01, low, high),\n",
        "#        stats.randint.ppf(0.99, low, high),1)\n",
        "# print(r)\n",
        "# P(X=x) --> 是機率\n",
        "probs = stats.randint.pmf(r,low,high)\n",
        "print(probs)\n",
        "plt.bar(r, probs)\n",
        "plt.ylabel('P(X=x)')\n",
        "plt.xlabel('x')\n",
        "plt.title('pmf of DU(1,6)')\n",
        "plt.show()"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[0.16666667 0.16666667 0.16666667 0.16666667 0.16666667 0.16666667]\n"
          ],
          "name": "stdout"
        },
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
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "id": "vKWJvSJeTY5x",
        "outputId": "c450f2b4-1c33-4610-ca6f-ad3fa0456fa2"
      },
      "source": [
        "# 3.計算離散均勻分配的累積機率 (cumulative density function)，pmf 的累加\n",
        "# P(X=x) --> 是機率\n",
        "cumsum_probs = stats.randint.cdf(r, low,high)\n",
        "plt.ylabel('P(X<=x)')\n",
        "plt.xlabel('x')\n",
        "plt.title(' cdf of DU(1,6)')\n",
        "plt.plot(r, cumsum_probs)\n",
        "plt.show()"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYIAAAEWCAYAAABrDZDcAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nO3dd3yVhfn+8c/NDCPsTQh7E1QMSy3iRqUijtZarRurP/u17bcCKipuXLVaV6m7Wq0lgIjgBrcIWElCGIYd9p4hZNy/P86h34igCeTJk5xzvV8vXsk55znPuY5Crjzj3I+5OyIiEr+qhB1ARETCpSIQEYlzKgIRkTinIhARiXMqAhGROKciEBGJcyoCiVlmNtjMcord7mpm35rZTjP7n1Kuy8zsBTPbamZfl33a771WDzObY2YWwLq/NrOeZb1eqdxUBBJPRgIz3D3R3R8v5XNPAE4Dkty934EPmtnlZlZoZruif5ZFi6NLsWW+V0zF7p9pZlcXu+tu4GGPfsjHzG6IFkOemb34U0HNrIOZTY0W3iYze7DYww8Dd5X4XUtcUBFIPGkLzD+C5y53990/ssyX7l4XqA+cCuQCc82sV0lfxMxaAicBk4vdvQa4B3i+BM+vAbwPfAS0AJKAV4otMgU4ycxalDSTxD4VgVQ6ZtbTzN43sy1mtt7MboneX8vMXozuvskC+hZ7zkdEfsA+Ef2NvctB1tvKzKZE15ttZtdE778KeBYYGH3unT+Wz90L3X2Ju18PfAyMLcXbOw34xt33FlvfRHefDGwuwfMvB9a4+5/dfbe773X39GLr2gvMBc4oRSaJcdXCDiBSGmaWCHxAZBfHz4HqQI/ow3cAHaN/6gDT9z/P3U82s5nAK+7+7CFW/zqQCbQCugHvm9kSd3/OzAqBq939hFJGngjcX4rlU4BFpXyN4gYAy81sOpEizAR+5+4ZxZZZABx1BK8hMUZbBFLZDAXWufsj0d92d7r7rOhjvwDudfct7r4KKPFxADNrAxwPjIqu91siWwG/OcK8a4BGpVi+AbDzCF4vCbiIyHtvBbwNvBndZbTfzujriAAqAql82gBLDvFYK2BVsdsrSrHeVsAWdy/+Q3gF0Lp08X6gNbAl+n0BkS2YA1UH8qPfbwUSj+D1coHP3H26u+8jsuXUGOhebJlEYNsRvIbEGBWBVDargA6HeGwtkaLYL7kU610DNIrueir+/NWli/cDw4FPo9+vBJqYWd39D0ZPEW3L/5VWOvCD4xelkA781Ejh7sC8I3gNiTEqAqlspgItzez3ZlbTzBLNrH/0sTeAm82soZklAb8r6Uqju5K+AO43swQz6w1cxffPuCkRM6tqZu3N7K/AYODO6GusBGYBD5hZXTOrCdxEZGvgq+jT3wf6mFlCsfVVi96uClSN5qtW7HE3s8HRm68AA8zsVDOrCvwe2ETkuADR9RwbfR0RQEUglUx0181pRA4UrwO+I3I2EER+4K4AlgHvAf8o5ep/BbQjsnUwCbjD3T8oxfMHmtkuYAcwE6gH9D3gQO0vgWZANpGtjVOAs/efJeTu64mc+jms2HPGENnlMxq4JPr9GPjvsY2dQEb0+YuiyzxDZDfTMOCc6G4iiPx3m+nua0rxviTGmS5MI1KxmFkP4CWgn//EP1AzuwTo6e43l3Dds4Cr3D3zyJNKrFARiIjEOe0aEhGJcyoCEZE4pyIQEYlzlW7ERJMmTbxdu3ZhxxARqVTmzp27yd2bHuyxSlcE7dq1Y86cOWHHEBGpVMzskJ+0164hEZE4pyIQEYlzKgIRkTinIhARiXMqAhGROBdYEZjZ82a2wcwOOtPEIh6PXhIw3cz6BJVFREQOLcgtgheBIT/y+JlA5+ifEcDTAWYREZFDCKwI3P0T/u/KTAczDHjZI74CGphZy6DyiIhUVrn7Crl/+gJytu4JZP1hHiNozfcvK5jDIS4LaGYjzGyOmc3ZuHFjuYQTEakIvliyiTP+8gl/+3gpMxYF8/OvUnyy2N3HA+MBUlNTNTdbRGLejr353D9tAa99vYp2jWvz+ogBDOjQOJDXCrMIVvP968smceTXhxURqfTez1rPmMkZbNyZx7UnduAPp3YhoXrVwF4vzCKYAtxgZq8D/YHt7r42xDwiIqHatCuPsVPmMzV9Ld1aJPL336TSO6lB4K8bWBGY2WtELtzdxMxygDuA6gDu/gwwDTiLyLVb9wBXBJVFRKQic3fe/HYNd741n915hfzvaV249sSO1KhWPodxAysCd//VTzzuwP8L6vVFRCqDNdtyGTM5k48WbuCY5AY8eH5vOjdPLNcMleJgsYhIrCkqcv759UrGTV9IYZFz+9AeXHZcO6pWsXLPoiIQESlnyzbtZlRaOl8v28IJnZpw/3kptGlUO7Q8KgIRkXJSUFjEs58t49H3F1OjWhUePL83F6YmYVb+WwHFqQhERMpB1podjEpLJ2P1dk7v0Zy7z+1F83oJYccCVAQiIoHKKyjkiY+yeXrmEhrUrs6TF/fhrJQWoW8FFKciEBEJyNwVWxmVlk72hl2c16c1t53dg4Z1aoQd6wdUBCIiZWx3XgEPv7eIF79YTqv6tXjxir4M7tos7FiHpCIQESlDn363kZsnZpCzNZffDGzLyCHdqFuzYv+ordjpREQqie178rl3WhZvzMmhQ5M6vHHtQPq1bxR2rBJREYiIHKF3Mtdx25uZbNm9j+sGd+TGUzoHOiSurKkIREQO08adkSFxb2espUfLerxweV96ta4fdqxSUxGIiJSSuzPxm9XcNTWL3PxCbjqjKyMGdaB61TCv9XX4VAQiIqWQs3UPt0zK5JPFGzm2bUMeOL83nZrVDTvWEVERiIiUQFGR88qsFTwwfSEO3HlOTy4d0JYqIQyJK2sqAhGRn7Bk4y5Gp6Uze/lWBnVpyn3De5HUMLwhcWVNRSAicgj5hUX8/dOl/OWD76hVvSoPX3gU5/dpXaHGQ5QFFYGIyEFkrt7OqLR05q/ZwVkpLRh7Tk+aJVaMIXFlTUUgIlLM3vxCHv/wO/72yVIa1q7BM5f0YUivlmHHCpSKQEQkas7yLYxMS2fpxt1ceGwSY87uQf3a1cOOFTgVgYjEvV15BTz0zkJe/moFrRvU4uUr+zGoS9OwY5UbFYGIxLWPF2/klokZrNmey2UD23HTGV2pU8GHxJW1+Hq3IiJR2/bs466pWUz8ZjUdm9Zhwm8HcmzbyjEkrqypCEQk7kzLWMvtb2aybU8+N5zUiRtO7lSphsSVNRWBiMSNDTv2cvub83ln/jp6ta7HS1f2o2eryjckrqypCEQk5rk7/56bwz1Ts8grKGL0md24+oT2VKukQ+LKmopARGLaqi17uGVSBp9+t4l+7Rox7vwUOjSt3EPiypqKQERiUmGR8/KXy3nwnUVUMbj73F78ul9yTAyJK2sqAhGJOdkbdjJyQjrfrNzG4K5NuXd4Cq0b1Ao7VoWlIhCRmJFfWMTfPl7C4x9mU7tmVR795VGce3TsDYkrayoCEYkJGTnbuWnCPBau28nQ3i0Ze05PmtStGXasSkFFICKV2t78Qh79YDHPfrqMxnVqMP7SYzm9Z4uwY1UqKgIRqbRmLd3M6IkZLNu0m4v6tuHms7pTv1bsD4krayoCEal0du7N54F3FvLKVytp06gWr17dn+M7NQk7VqWlIhCRSmXGwg3cOimDtTv2ctUJ7fnf07tQu4Z+lB0J/dcTkUphy+593D01i0n/WU3nZnVJu+44+iQ3DDtWTFARiEiF5u68nbGWO96cz/bcfG48pTPXn9SRmtXid0hcWVMRiEiFtX7HXsZMzuT9rPX0TqrPq9f0p1uLemHHijkqAhGpcNydf81exb3TFrCvoIhbz+rOFce305C4gKgIRKRCWbl5D6MnpvPFks30b9+IB87vTbsmdcKOFdMCLQIzGwI8BlQFnnX3cQc8ngy8BDSILjPa3acFmUlEKqbCIueFz5fx8HuLqFalCvcNT+Givm00JK4cBFYEZlYVeBI4DcgBZpvZFHfPKrbYGOANd3/azHoA04B2QWUSkYpp8frIkLhvV23j5G7NuHd4L1rW15C48hLkFkE/INvdlwKY2evAMKB4ETiw/8hPfWBNgHlEpILZV1DE0zOX8MSM70hMqM5jFx3NOUe10pC4chZkEbQGVhW7nQP0P2CZscB7ZvY7oA5w6sFWZGYjgBEAycnJZR5URMrfvFXbGDkhnUXrdzLs6FbcPrQHjTUkLhRhHyz+FfCiuz9iZgOBf5hZL3cvKr6Qu48HxgOkpqZ6CDlFpIzk7ivkz+8v4rnPltEsMYFnf5PKqT2ahx0rrgVZBKuBNsVuJ0XvK+4qYAiAu39pZglAE2BDgLlEJCRfLtnM6InprNi8h4v7JzP6zG7US9CQuLAFWQSzgc5m1p5IAVwEXHzAMiuBU4AXzaw7kABsDDCTiIRgx9587p+2kNe+XknbxrX55zX9Oa6jhsRVFIEVgbsXmNkNwLtETg193t3nm9ldwBx3nwL8L/B3M/sDkQPHl7u7dv2IxJAPF6zn1kmZbNi5lxGDOvCHU7tQq4bGQ1QkgR4jiH4mYNoB991e7Pss4PggM4hIODbvyuPOt7KYMm8N3Vok8rdLj+WoNg3CjiUHEfbBYhGJMe7OlHlruPOtLHbuzecPp3bhusEdqVFN4yEqKhWBiJSZtdtzGTMpkw8XbuDoNg148ILedGmeGHYs+QkqAhE5YkVFzmuzV3L/tIUUFBUx5uzuXHF8e6pqPESloCIQkSOyfNNuRk9M56ulWziuY2PGndeb5Ma1w44lpaAiEJHDUlBYxPOfL+OR9xZTo2oVxp2Xwi/7ttF4iEpIRSAipbZw3Q5GTUhnXs52Tu3enHvO7UWL+glhx5LDpCIQkRLLKyjkyRlLeGpGNvVrVeeJi4/h7JSW2gqo5FQEIlIi/1m5lVFp6Sxev4vhx7Tm9qE9aFinRtixpAyoCETkR+3ZV8Aj7y3m+c+X0aJeAi9c3peTujULO5aUIRWBiBzS59mbGD0xnVVbcrlkQDKjhnQjUUPiYo6KQER+YHtuPvdPW8Drs1fRvkkd/jViAP07NA47lgRERSAi3/Pe/HWMmZzJpl15XHtiZEhcQnUNiYtlKgIRAWDTrjzGTpnP1PS1dGuRyLOXpdI7SUPi4oGKQCTOuTuTv13NnW9lsSevkD+d3oVrT+xI9aoaEhcvVAQicWz1tlxunZTBzEUb6ZMcGRLXqZmGxMUbFYFIHCoqcl79eiXjpi2gyOGOn/fgNwPbaUhcnFIRiMSZpRt3MTotg6+Xb+GETk24/7wU2jTSkLh4piIQiRMFhUU8+9kyHn1/MTWrVeHBC3pz4bFJGg8hKgKReJC1Zgcj0+aRuXoHZ/Rszt3DetGsnobESYSKQCSG5RUU8sRH2Tw9cwkNatfg6V/34cyUlmHHkgpGRSASo+au2MKotAyyN+zi/D5J3Da0Ow1qa0ic/JCKQCTG7M4r4KF3F/HSl8tpVb8WL13ZjxO7NA07llRgKgKRGPLpdxu5eWIGOVtzuWxgW24a0o26NfXPXH6c/oaIxIDte/K55+0s/j03hw5N6/Dv3w6kb7tGYceSSkJFIFLJvZO5jtvezGTL7n1cP7gj/3NKZw2Jk1JREYhUUht27mXslPlMy1hHj5b1eOHyvvRqXT/sWFIJlbgIzKwKcBTQCsgFMt19Q1DBROTg3J20b1Zz99QscvMLuemMrowY1EFD4uSw/WQRmFlHYBRwKvAdsBFIALqY2R7gb8BL7l4UZFARgZyte7hlUiafLN5IatuGjDu/N52a1Q07llRyJdkiuAd4GrjW3b34A2bWDLgYuBR4qezjiQhEhsT946sVPPDOQgDuPKcnlw5oSxUNiZMy8JNF4O6/+pHHNgB/KdNEIvI9SzbuYtSEdOas2MqgLk25b3gvkhpqSJyUnRLvVDSzu82sWrHb9czshWBiiUh+YRFPzsjmzMc+5bsNu3jkwqN46Yq+KgEpc6U5a6gaMMvMrgCaA08Afw0klUicy1y9nVFp6cxfs4OzUlpw5zm9aJpYM+xYEqNKXATufrOZfQDMArYCg9w9O7BkInFob34hj3/4HX/7ZCmN6tTgmUv6MKSXhsRJsEpz+ugg4HHgLiAF+KuZXeXua4IKJxJPZi/fwqgJ6SzdtJsLj01izNk9qF+7etixJA6UZtfQw8CF7p4FYGbnAR8B3YIIJhIvduUV8OA7C3n5yxUkNazFP67qx886a0iclJ/SFMFAdy/cf8PdJ5rZxwFkEokbHy/eyC0TM1izPZfLj2vHTWd0pY6GxEk5K80xgkIzO9ndP9r/1d03BxlOJFZt27OPu6ZmMfGb1XRsWocJvx3IsW01JE7CUdpfPR4G+hT7KiKl4O5Mz1zH7W9msm1PPr87uRM3nNyJmtU0JE7Cc7jboCX6OKOZDQEeA6oCz7r7uIMs8wtgLODAPHe/+DAziVRoG3bs5bY3M3l3/npSWtfn5Sv706NVvbBjiQQ3fdTMqgJPAqcBOcBsM5uy/2BzdJnOwM3A8e6+NTqyQiSmuDv/npvDPVOzyCsoYvSZ3bj6hPZU05A4qSCCPCrVD8h296UAZvY6MAzIKrbMNcCT7r4V/juyQiRmrNqyh5snZvBZ9ib6tWvEuPNT6NBUQ+KkYgmyCFoDq4rdzgH6H7BMFwAz+5zI7qOx7v7OgSsysxHACIDk5ORAwoqUpcIi5+Uvl/PgO4uoYnD3ub34db9kDYmTCqm0RbAr+nVnGb5+Z2AwkAR8YmYp7r6t+ELuPh4YD5CamuoHrkSkIsnesJORE9L5ZuU2Bndtyr3DU2jdoFbYsUQOqVRF4O6Din/9CauBNsVuJ0XvKy4HmOXu+cAyM1tMpBhmlyaXSEWQX1jEMzOX8NePsqlTsyp/+eXRDDu6FWbaCpCKLchdQ7OBzmbWnkgBXETk2gXFTQZ+BbxgZk2I7CpaGmAmkUBk5GznpgnzWLhuJ0N7t2TsOT1pUldD4qRyKFERmFlD4Gugy/6L05jZy8C/3f2tgz3H3QvM7AbgXSL7/5939/lmdhcwx92nRB873cyygELgJn1ITSqTvfmFPPrBYv7+yVKa1K3J+EuP5fSeLcKOJVIqdsBFxw69oNmrwCvuPt3MEoH/ECmGcr1EZWpqqs+ZM6c8X1LkoGYt3czoiRks27Sbi/q24eazulO/lobEScVkZnPdPfVgj5Vm19CzwPXAdOCXRLYGdJ1iiTs79+bzwDsLeeWrlSQ3qs2rV/fn+E5Nwo4lcthKM2tohpk9aWaNgMuAywNLJVJBzVi4gVsmZbB+x16uPqE9fzy9C7VraEicVG6l/Rv8DyIXsy909yUB5BGpkLbs3sddb81n8rdr6NysLk9ddxzHJDcMO5ZImShtEbwIrASuLPsoIhWPuzM1fS1jp8xne24+N57SmetP6qghcRJTSvs5grVmdhyQHlAekQpj/Y693Dopkw8WrKd3Un1evaY/3VpoSJzEnp8sAjOr6+77P1GMu88u9lhH7SKSWOPu/Gv2Ku6dtoB9BUXcelZ3rji+nYbEScwqyRbBPDO72d3f2H+HmSUAY4h8SKxTUOFEytvKzXsYPTGdL5ZsZkCHRow7rzftmtQJO5ZIoEpSBKcDT5jZ1UROH+1J5MI0k4GjA8wmUm4Ki5wXPl/Gw+8tonqVKtw3PIWL+rbRkDiJCz9ZBNFdP2ea2U3AQmAdcIa7zw86nEh5WLRuJyPT0pm3ahundGvGPcN70bK+hsRJ/CjJMYJqwE3A/i2Cs4DHzex6d18UcD6RwOwrKOKpmdk8OSObxITqPHbR0ZxzlIbESfwpya6hb4GZQB933w6MN7OhwBQzS3P3W4IMKBKEeau2MXJCOovW72TY0a24fWgPGmtInMSpkhTBZe4+t/gd7j7VzD4kcsBYpNLI3VfIn99fxHOfLaNZYgLPXZbKKd2bhx1LJFQlKYJvDnanu+cCtwKYmXlJp9eJhOSLJZu4eWIGKzbv4eL+yYw+sxv1EjQkTqQkRTDDzNKAN9195f47zawGcAKRuUMziHzqWKTC2bE3n/unLeS1r1fStnFtXrtmAAM7Ng47lkiFUZIiGEJkpMRr0YvMbAMSiFxj4D3gL+7+n+Aiihy+D7LWc+vkDDbuzGPEoA784dQu1Kqh8RAixZXk9NG9wFPAU2ZWHWgC5B54XWGRimTzrjzufCuLKfPW0K1FIuMvTeWoNg3CjiVSIZXk9NEE4LdEPkGcTuRKYwVBBxM5HO7OlHlrGDtlPrvyCvjDqV24bnBHalTTeAiRQynJrqGXgHzgUyKfIegJ3BhkKJHDsXZ7LmMmZfLhwg0c3aYBD17Qmy7NE8OOJVLhlaQIerh7CoCZPUfk2sUiFUZRkfPa7JXcP20hhUXOmLO7c8Xx7amq8RAiJVKSIsjf/030gvQBxhEpnWWbdjM6LZ1Zy7ZwfKfG3D+8N8mNa4cdS6RSKUkRHGVmO6LfG1AretsAd3cNaJdyV1BYxPOfL+OR9xZTo1oVHjg/hV+kttF4CJHDUJKzhnSunVQoC9buYFRaOuk52zmtR3PuObcXzeslhB1LpNLSVbel0sgrKOTJGUt4akY29WtV54mLj+HslJbaChA5QioCqRS+WbmVURPS+W7DLs47pjW3De1Bwzo1wo4lEhNUBFKh7dlXwCPvLeb5z5fRsl4CL1zRl5O6Ngs7lkhMURFIhfV59iZGT0xn1ZZcLh3QlpFDupKoIXEiZU5FIBXO9tx87nt7Af+as4r2TerwrxED6N9BQ+JEgqIikArlvfnrGDM5k8279/HbEzvy+1M7k1BdJ66JBElFIBXCxp15jH1rPm+nr6V7y3o8d1lfUpLqhx1LJC6oCCRU7s7kb1dz51tZ7Mkr5E+nd+HaEztSvaqGxImUFxWBhGb1tlxunZTBzEUb6ZMcGRLXqZmGxImUNxWBlLuiIufVWSsYN30hDoz9eQ8uHdhOQ+JEQqIikHK1dOMuRqdl8PXyLfyscxPuG55Cm0YaEicSJhWBlIuCwiL+/ukyHv1gMQnVqvDQBb254NgkjYcQqQBUBBK4rDU7GJk2j8zVOzijZ3PuHtaLZhoSJ1JhqAgkMHvzC3nio2ye+XgJDWrX4Olf9+HMlJZhxxKRA6gIJBBzV2xh5IR0lmzczfl9krhtaHca1NaQOJGKSEUgZWp3XgEPvbuIl75cTqv6tXjpyn6c2KVp2LFE5EcE+qkdMxtiZovMLNvMRv/IcuebmZtZapB5JFifLN7I6Y9+wktfLuc3A9ry7h8GqQREKoHAtgjMrCrwJHAakAPMNrMp7p51wHKJwI3ArKCySLC278nn7rezmDA3hw5N6/DGtQPp265R2LFEpISC3DXUD8h296UAZvY6MAzIOmC5u4EHgJsCzCIBeSdzLbe9OZ8tu/dx/eCO/M8pGhInUtkEWQStgVXFbucA/YsvYGZ9gDbu/raZqQgqkQ0793LHm/OZnrmOHi3r8cLlfenVWkPiRCqj0A4Wm1kV4M/A5SVYdgQwAiA5OTnYYPKj3J20b1Zz99QscvMLGTmkK9f8rIOGxIlUYkEWwWqgTbHbSdH79ksEegEzo58ubQFMMbNz3H1O8RW5+3hgPEBqaqoHmFl+RM7WPdwyKZNPFm+kb7uGjDu/Nx2b1g07logcoSCLYDbQ2czaEymAi4CL9z/o7tuBJvtvm9lM4E8HloCEr6jI+cdXK3jgnYUYcNewnlzSvy1VNCROJCYEVgTuXmBmNwDvAlWB5919vpndBcxx9ylBvbaUnewNuxidls6cFVsZ1KUp9w3vRVJDDYkTiSWBHiNw92nAtAPuu/0Qyw4OMouUTn5hEeM/WcpjH3xHrRpVeeTCozivT2sNiROJQfpksfxA5urtjJyQTtbaHZyV0oI7z+lF08SaYccSkYCoCOS/9uYX8tiH3zH+k6U0qlODZy7pw5BeGhInEutUBALA7OVbGDUhnaWbdvOL1CRuPasH9WtXDzuWiJQDFUGc25VXwIPvLOTlL1eQ1LAWr1zVnxM6N/npJ4pIzFARxLGZizZw66RM1mzP5Yrj2/Gn07tSp6b+SojEG/2rj0Nbd+/j7rezmPjNajo1q8uE3x7HsW0bhh1LREKiIogj7s70zHXc/mYm2/bk87uTO3HDyZ2oWU1D4kTimYogTmzYsZfb3szk3fnrSWldn5ev7E+PVvXCjiUiFYCKIMa5O/+em8M9U7PIKyji5jO7cdUJ7ammIXEiEqUiiGGrtuzh5okZfJa9iX7tGzHuvBQ6aEiciBxARRCDCoucl75YzkPvLqJqFeOec3txcb9kDYkTkYNSEcSY79bvZFRaOt+s3Mbgrk25d3gKrRvUCjuWiFRgKoIYkV9YxDMzl/DXj7KpU7Mqf/nl0Qw7upWGxInIT1IRxICMnO3cNGEeC9ftZGjvlow9pydN6mpInIiUjIqgEtubX8ijHyzm758spWliTcZfeiyn92wRdiwRqWRUBJXUV0s3MzotneWb9/Crfm0YfWZ36tfSkDgRKT0VQSWzc28+46Yv5NVZK0luVJt/Xt2f4zppSJyIHD4VQSUyY+EGbpmUwfode7n6hPb88fQu1K6h/4UicmT0U6QS2LJ7H3e9NZ/J366hc7O6PHXdcRyTrCFxIlI2VAQVmLszNX0tY6fMZ3tuPjee0pnrT+qoIXEiUqZUBBXUuu17GTM5kw8WrOeopPq8ek1/urXQkDgRKXsqggrG3Xl99irue3sB+UVF3HpWd648oT1VNR5CRAKiIqhAVmzezei0DL5cupkBHRox7rzetGtSJ+xYIhLjVAQVQGGR88Lny3j4vUVUr1KF+4ancFHfNhoSJyLlQkUQskXrdjIyLZ15q7ZxSrdm3DO8Fy3ra0iciJQfFUFI9hUU8dTMbJ6ckU1iQnUe/9Ux/Lx3Sw2JE5FypyIIwbertjFqQjqL1u9k2NGtuOPnPWlUp0bYsUQkTqkIylHuvkL+/P4invtsGc0SE3juslRO6d487FgiEudUBOXkiyWbGJ2Wwcote7i4fzKjz+xGvQQNiROR8KkIArZjbz73T1vIa1+vpG3j2rx2zQAGdmwcdiwRkf9SEQTog6z13MBxMk4AAAdPSURBVDo5g4078xgxqAN/OLULtWpoPISIVCwqggBs3pXH2LeyeGveGrq1SGT8pakc1aZB2LFERA5KRVCG3J0p89Ywdsp8duUV8MfTuvDbEztSo1qVsKOJiBySiqCMrNmWy5jJmXy0cANHt2nAgxf0pkvzxLBjiYj8JBXBESoqcv759UrGTV9IYZFz29AeXH5cOw2JE5FKQ0VwBJZt2s3otHRmLdvC8Z0ac//w3iQ3rh12LBGRUlERHIaCwiKe+2wZf35/MTWqVeGB81P4RWobjYcQkUpJRVBKC9buYFRaOuk52zmtR3PuObcXzeslhB1LROSwqQhKKK+gkCc/yuapmUtoULs6T17ch7NSWmgrQEQqvUCLwMyGAI8BVYFn3X3cAY//EbgaKAA2Ale6+4ogMx2OuSu2MiotnewNuzjvmNbcNrQHDTUkTkRiRGBFYGZVgSeB04AcYLaZTXH3rGKL/QdIdfc9ZnYd8CDwy6AyldaefQU89O4iXvxiOS3rJfDCFX05qWuzsGOJiJSpILcI+gHZ7r4UwMxeB4YB/y0Cd59RbPmvgEsCzFMqn323idET08nZmsulA9oyckhXEjUkTkRiUJBF0BpYVex2DtD/R5a/Cph+sAfMbAQwAiA5Obms8h3U9tx87n07izfm5NC+SR3+NWIA/TtoSJyIxK4KcbDYzC4BUoETD/a4u48HxgOkpqZ6UDnenb+O2yZnsnn3Pq4b3JEbT+lMQnUNiROR2BZkEawG2hS7nRS973vM7FTgVuBEd88LMM8hbdyZx9gp83k7Yy3dW9bjucv6kpJUP4woIiLlLsgimA10NrP2RArgIuDi4guY2THA34Ah7r4hwCwH5e5M/GY1d03NIndfITed0ZURgzpQvaqGxIlI/AisCNy9wMxuAN4lcvro8+4+38zuAua4+xTgIaAu8O/o+fgr3f2coDIVt3pbLrdMzODjxRvpkxwZEtepmYbEiUj8CfQYgbtPA6YdcN/txb4/NcjXP5iiIueVWSt4YPpCHBj78x5cOlBD4kQkflWIg8XlZcnGXYxOS2f28q38rHMT7hueQptGGhInIvEtborgjdmrGPNmJgnVqvDQBb254NgkjYcQESGOiqB90zqc0q0Zdw7rSbNEDYkTEdkvboqgb7tG9G3XKOwYIiIVjs6TFBGJcyoCEZE4pyIQEYlzKgIRkTinIhARiXMqAhGROKciEBGJcyoCEZE4Z+6BXeclEGa2ETjcC9w3ATaVYZzKQO85Pug9x4cjec9t3b3pwR6odEVwJMxsjrunhp2jPOk9xwe95/gQ1HvWriERkTinIhARiXPxVgTjww4QAr3n+KD3HB8Cec9xdYxARER+KN62CERE5AAqAhGROBcXRWBmz5vZBjPLDDtLeTGzNmY2w8yyzGy+md0YdqagmVmCmX1tZvOi7/nOsDOVBzOramb/MbOpYWcpD2a23MwyzOxbM5sTdp7yYGYNzGyCmS00swVmNrBM1x8PxwjMbBCwC3jZ3XuFnac8mFlLoKW7f2NmicBc4Fx3zwo5WmAschHqOu6+y8yqA58BN7r7VyFHC5SZ/RFIBeq5+9Cw8wTNzJYDqe4eNx8mM7OXgE/d/VkzqwHUdvdtZbX+uNgicPdPgC1h5yhP7r7W3b+Jfr8TWAC0DjdVsDxiV/Rm9eifmP5Nx8ySgLOBZ8POIsEws/rAIOA5AHffV5YlAHFSBPHOzNoBxwCzwk0SvOhukm+BDcD77h7r7/kvwEigKOwg5ciB98xsrpmNCDtMOWgPbAReiO4CfNbM6pTlC6gIYpyZ1QXSgN+7+46w8wTN3Qvd/WggCehnZjG7K9DMhgIb3H1u2FnK2Qnu3gc4E/h/0V2/sawa0Ad42t2PAXYDo8vyBVQEMSy6nzwNeNXdJ4adpzxFN51nAEPCzhKg44FzovvMXwdONrNXwo0UPHdfHf26AZgE9As3UeBygJxiW7cTiBRDmVERxKjogdPngAXu/uew85QHM2tqZg2i39cCTgMWhpsqOO5+s7snuXs74CLgI3e/JORYgTKzOtGTH4juHjkdiOmzAd19HbDKzLpG7zoFKNOTPqqV5coqKjN7DRgMNDGzHOAOd38u3FSBOx64FMiI7jMHuMXdp4WYKWgtgZfMrCqRX3LecPe4OKUyjjQHJkV+z6Ea8E93fyfcSOXid8Cr0TOGlgJXlOXK4+L0UREROTTtGhIRiXMqAhGROKciEBGJcyoCEZE4pyIQEYlzKgIRkTinIhARiXMqApEjZGZ9zSw9ej2EOtFrIcTsjCOJPfpAmUgZMLN7gASgFpG5MPeHHEmkxFQEImUg+tH/2cBe4Dh3Lww5kkiJadeQSNloDNQFEolsGYhUGtoiECkDZjaFyCjo9kQuEXpDyJFESiwupo+KBMnMfgPku/s/o5NPvzCzk939o7CziZSEtghEROKcjhGIiMQ5FYGISJxTEYiIxDkVgYhInFMRiIjEORWBiEicUxGIiMS5/w/2UapsrC99HAAAAABJRU5ErkJggg==\n",
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
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "i9kB2fzZTeba",
        "outputId": "0c8c7b00-42bb-4486-b388-dd8c996d8772"
      },
      "source": [
        "# 4.透過 cdf ，給定一個 機率值，反推出對應到的 x\n",
        "k = stats.randint.ppf(cumsum_probs , low, high)\n",
        "print(k)\n",
        "#看上圖看結果"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[1. 2. 3. 4. 5. 6.]\n"
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
          "height": 283
        },
        "id": "pD1nYoz_TlOk",
        "outputId": "7a40f3f7-fa4c-4c85-8e7b-b8f2fc5e7920"
      },
      "source": [
        "# 5.產生符合隨機樣本點 (random sample)\n",
        "X = stats.randint.rvs(low,high,size=20)\n",
        "print(X)\n",
        "plt.hist(X,bins=13)\n",
        "plt.show()\n",
        "#試試看，，每一次的結果一樣嗎?"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[6 3 3 3 6 1 1 3 3 5 2 4 6 2 2 3 6 3 6 2]\n"
          ],
          "name": "stdout"
        },
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
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "s2QNeJ4zTuxR",
        "outputId": "f5fa552a-72ec-40e5-dac1-fb20571b0103"
      },
      "source": [
        "#6.計算固定參數下，隨機變數的平均數、變異數、偏度和峰度。\n",
        "stat_randint=stats.randint.stats(low,high,moments='mvks')\n",
        "print(stat_randint)\n",
        "print(type(stat_randint))\n",
        "# 平均數\n",
        "print(\"randint mean=\",float(stat_randint[0]))\n",
        "# 變異數\n",
        "print(\"randint variance=\",float(stat_randint[1]))\n",
        "# 偏度\n",
        "print(\"randint kurtosis=\",float(stat_randint[2]))\n",
        "# 峰度\n",
        "print(\"randint skew=\",float(stat_randint[3]))"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "(array(3.5), array(2.91666667), array(0.), array(-1.26857143))\n",
            "<class 'tuple'>\n",
            "randint mean= 3.5\n",
            "randint variance= 2.9166666666666665\n",
            "randint kurtosis= 0.0\n",
            "randint skew= -1.2685714285714285\n"
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
          "height": 295
        },
        "id": "RkdtXDmsT9zQ",
        "outputId": "0612f799-5697-4cc0-b59c-7cd4f11d3852"
      },
      "source": [
        "'''\n",
        "# 伯努利分配( Bernoulli Distribution )\n",
        "# 前提：是只有兩種可能結果（成功或失敗）的單次隨機試驗，成功的機率為p\n",
        "'''\n",
        "# ①定義伯努利分配的基本資訊\n",
        "\n",
        "# ①定義伯努利分配基本資訊\n",
        "p = 0.4 # 事件A 機率 0.4\n",
        "r = np.arange(0,2) # 可以出現的範圍為 0、1, 2種可能出現的結果\n",
        "\n",
        "# ②計算二項分佈的概率質量分佈 (probability mass function)\n",
        "# 之所以稱為質量，是因為離散的點\n",
        "# P(X=x) --> 是機率\n",
        "probs = stats.bernoulli.pmf(r,p)\n",
        "#array([ 0.07776, 0.2592 , 0.3456 , 0.2304 , 0.0768 , 0.01024])\n",
        "plt.bar(r, probs)\n",
        "plt.ylabel('P(X=x)')\n",
        "plt.xlabel('x')\n",
        "plt.title('Bernoulli(p=0.4)')\n",
        "plt.show()"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYIAAAEWCAYAAABrDZDcAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAXMUlEQVR4nO3dfbRddX3n8ffHxIAKFixREQJBibbxCTWiy/G5dAxaEzo6GlqX0OJEp0Xb2uUYygzjZKyC1uLqFKdSa0VbjUinnVjSIgrUsRZMaHkwYDREKkGRiPhAVSD4nT/Ovro5nJvcm9x9T272+7XWWWfv3/7tfb5n5+Z8zt6/c/ZJVSFJ6q8HjbsASdJ4GQSS1HMGgST1nEEgST1nEEhSzxkEktRzBoE0TUkqybHN9IeSvL2Zfl6SLUN935nkt8dR51Qk+UKSJ467Do2XQaB9RpKbk/wwyV1J7kxycZJF465rqqrq/1XVEybmkywEXgu8fyYfJwPnJLmjuZ2TJFNY74PtEGv8AbB2JuvT3GMQaF/z8qo6CDgc+Cbwv6a7gSTzZ7yqPXMqsKGqfjjD210NnAQ8FXgK8HLg9btaIclzgceNWLQeeFGSR89wjZpDDALtk6rqR8BFwFKAJAck+YMkX0vyzSR/kuQhzbIXJtme5K1JbgP+PMnbklyY5MNJvp9kc5JlE9tP8vNJrkjynWbZitayK5K8rjV/apLP7a7miTpaTScC/zC8PMnvJflWcwT0q3uwe04B3lNV26vqVuA9DEJnsrrmMwjUNw4va/bz1cBL9qAO7ScMAu2TkjwUeDVwZdN0NvB44DjgWOAI4KzWKo8GHgEczeAdM8AKYB1wCIN3vn/cbPvBwCeBTwGPZPAC+ZdJnsDMejKwZajt0cBhTf2nAOdPPG6SNU0wjby1tvFE4NrW/LVN22R+B/hsVV03yfIbGRxdqKcMAu1r/qZ50fsu8IvAu5vz36uB36mqb1fV94F3AKta6/0Y+O9VdXfrVMznqmpDVd0HfISfvtg9GzgIOLuq7qmqy4C/BU6e4edyCPD9Ee3/ranzH4CLgVcBVNXZVXXIZLfW+gcx2D8TvgscNGqcoBljeT33D81h329qVU/tK+dSpQknVdWnk8wDVjI4tXIc8FDg6tZrXYB5rfV2NKc52m5rTf8AOLA5TfIY4Jaq+nFr+b8yeJc+k+4EDh5uq6p/G3rcx0xzu3cBD2/NPxy4q0ZfQfK9wNqq+u6IZRMOBr6zi+Xaz3lEoH1SVd1XVf8HuI/BO/gfAk9svUP+mWZQ+SerTGPzXwcWJWn//R8F3NpM/xuD4JmwpwOp1zE4ndV2aJKHDT3u1wGasYO7Jru11tnM/U/lPLVpG+UXGBxV3daMnwD8U5JfafX5ee5/qkk9YxBon9R8RHIlcCiDF7k/Bc5N8shm+RFJ9nSA8yoGRwj/JcmDk7yQwSdv1jXLrwH+Q5KHNh+1PG0PH2cD8IIR7f8jyYIkzwN+CfgEQFW9o6oOmuzWWv/DwJubffAY4HeBD01Sw+MZBMVxzY3muf41QJIDgWcAl+7hc9R+wCDQvuaTzbvf7wG/D5xSVZuBtwJbgSuTfA/4NLBHg7tVdQ+DF8MTgW8B7wNeW1VfarqcC9zD4OOrFwB/uYfP5cPASyc+3dS4jcEpo683231D63Gn6v0MBruvB77IYJzhJ99VaI4gngdQVbdX1W0Tt6bLt1rjKC8Hrqiqr0+zBu1H4g/TSN1J8g7g9qp6b3Pk8RdVdeSYy/qJJFcBp1XVF8ddi8bHwWKpQ1X1e+OuYVeq6lnjrkHj56khSeo5Tw1JUs95RCBJPTfnxggOO+ywWrx48bjLkKQ55eqrr/5WVS0ctWzOBcHixYvZtGnTuMuQpDklyb9OtsxTQ5LUcwaBJPWcQSBJPWcQSFLPGQSS1HMGgST1XKdBkGR5ki1JtiZZM0mfVyW5ofnd2I92WY8k6YE6+x5B8wtT5zH4ucHtwMYk66vqhlafJcAZwL+rqjsnrjUvSZo9XR4RHA9sraptzfXf1zH46cG2/wScV1V3wuDa6R3WI0kaoctvFh8B3NKa3w4MX/L28QBJ/pHB78++rar+fnhDSVYz+PFyjjrqqD0uaPGai/d4Xe3/bj77ZeMuQRqLcQ8WzweWAC8ETgb+NMkhw52q6vyqWlZVyxYuHHmpDEnSHuoyCG4FFrXmj+SnPw4+YTuwvqruraqvAl9mEAySpFnSZRBsBJYkOSbJAmAVsH6oz98wOBogyWEMThVt67AmSdKQzoKgqnYCpwOXADcCF1bV5iRrk6xoul0C3JHkBuBy4C1VdUdXNUmSHqjTy1BX1QZgw1DbWa3pAt7c3CRJYzDuwWJJ0pgZBJLUcwaBJPWcQSBJPWcQSFLPGQSS1HMGgST1nEEgST1nEEhSzxkEktRzBoEk9ZxBIEk9ZxBIUs8ZBJLUcwaBJPWcQSBJPWcQSFLPGQSS1HMGgST1nEEgST1nEEhSzxkEktRzBoEk9ZxBIEk9ZxBIUs91GgRJlifZkmRrkjUjlp+aZEeSa5rb67qsR5L0QPO72nCSecB5wC8C24GNSdZX1Q1DXT9eVad3VYckade6PCI4HthaVduq6h5gHbCyw8eTJO2BLoPgCOCW1vz2pm3YK5Jcl+SiJItGbSjJ6iSbkmzasWNHF7VKUm+Ne7D4k8DiqnoKcClwwahOVXV+VS2rqmULFy6c1QIlaX/XZRDcCrTf4R/ZtP1EVd1RVXc3sx8AntFhPZKkEboMgo3AkiTHJFkArALWtzskObw1uwK4scN6JEkjdPapoarameR04BJgHvDBqtqcZC2wqarWA29KsgLYCXwbOLWreiRJo3UWBABVtQHYMNR2Vmv6DOCMLmuQJO3auAeLJUljZhBIUs8ZBJLUcwaBJPWcQSBJPWcQSFLPGQSS1HMGgST1nEEgST1nEEhSzxkEktRzBoEk9ZxBIEk9ZxBIUs8ZBJLUcwaBJPWcQSBJPWcQSFLPGQSS1HMGgST1nEEgST1nEEhSzxkEktRzBoEk9ZxBIEk9ZxBIUs91GgRJlifZkmRrkjW76PeKJJVkWZf1SJIeqLMgSDIPOA84EVgKnJxk6Yh+BwO/BVzVVS2SpMl1eURwPLC1qrZV1T3AOmDliH7/EzgH+FGHtUiSJjG/w20fAdzSmt8OPKvdIcnTgUVVdXGSt0y2oSSrgdUARx11VAelSvuGxWsuHncJ2ofdfPbLOtnu2AaLkzwI+EPgd3fXt6rOr6plVbVs4cKF3RcnST3SZRDcCixqzR/ZtE04GHgScEWSm4FnA+sdMJak2dVlEGwEliQ5JskCYBWwfmJhVX23qg6rqsVVtRi4ElhRVZs6rEmSNKSzIKiqncDpwCXAjcCFVbU5ydokK7p6XEnS9HQ5WExVbQA2DLWdNUnfF3ZZiyRpNL9ZLEk9ZxBIUs8ZBJLUcwaBJPWcQSBJPWcQSFLPGQSS1HMGgST13LSDIMnDmt8akCTtB3YbBEkelORXklyc5HbgS8A3ktyQ5N1Jju2+TElSV6ZyRHA58DjgDODRVbWoqh4JPJfBheLOSfKaDmuUJHVoKtcaOqGq7h1urKpvA38F/FWSB894ZZKkWbHbI4KJEEhywvCyJKe0+0iS5p7pDBafleR/N4PFj0rySeDlXRUmSZod0wmCFwA3AdcAnwM+WlWv7KQqSdKsmU4QHAoczyAM7gaOTpJOqpIkzZrpBMGVwN9X1XLgmcBjgH/spCpJ0qyZzi+UnVBVXwOoqh8Cb0ry/G7KkiTNlikfEVTV15I8HGDivqo+21VhkqTZMd1LTFwxdC9JmuP29KJzDhJL0n7Cq49KUs8ZBJLUc3saBDWjVUiSxma6QZChe0nSHDfdIHj10P0uJVmeZEuSrUnWjFj+hiTXJ7kmyeeSLJ1mPZKkvTSVH6Y5aGK6qr7cvk/yuF2sNw84DzgRWAqcPOKF/qNV9eSqOg54F/CH034GkqS9MpUjgmuTvKrdkOTAJG8HLtnFescDW6tqW1XdA6wDVrY7VNX3WrMPw7EHSZp1UwmCfw/8WpJPJTk2yUrgeuAA4LhdrHcEcEtrfnvTdj9JfjPJTQyOCN40akNJVifZlGTTjh07plCyJGmqpvLDNDdV1YnApQx+r/g84KSqektV3bW3BVTVeVX1OOCtwH+dpM/5VbWsqpYtXLhwbx9SktQylTGC+UnOAN4A/AawCfijJE/Yzaq3Aota80c2bZNZB5y0u3okSTNrKqeGrmFwSufpzTvzk4BzgfVJ3rGL9TYCS5Ick2QBsApY3+6QZElr9mXAV6ZVvSRpr03lMtSnVNXV7Yaq+tskn2GSUzlNn51JTmcwoDwP+GBVbU6yFthUVeuB05vfQr4XuBM4ZU+fiCRpz0wlCP55VGPzmwRnAiRJVT3gEz9VtQHYMNR2Vmv6t6ZVrSRpxk3l1NDlSd6Y5Kh2Y5IFSV6c5AJ8Jy9Jc9ZUjgiWA78OfCzJMcB3gAMZnO75FPDeqvqX7kqUJHVpt0FQVT8C3ge8L8mDgcOAH1bVd7ouTpLUvd0GQZIDGXx09FjgOgaDvju7LkySNDumMkZwAbCMwbeJXwq8p9OKJEmzaipjBEur6skASf4M+EK3JUmSZtNUjgjunZjwlJAk7X+mckTw1CQTVwkN8JBmPkBV1cM7q06S1LmpfGpo3mwUIkkaD3+8XpJ6ziCQpJ4zCCSp5wwCSeo5g0CSes4gkKSeMwgkqecMAknqOYNAknrOIJCknjMIJKnnDAJJ6jmDQJJ6ziCQpJ4zCCSp5wwCSeo5g0CSeq7TIEiyPMmWJFuTrBmx/M1JbkhyXZLPJDm6y3okSQ/UWRAkmQecB5wILAVOTrJ0qNu/AMuq6inARcC7uqpHkjRal0cExwNbq2pbVd0DrANWtjtU1eVV9YNm9krgyA7rkSSN0GUQHAHc0prf3rRN5jTg70YtSLI6yaYkm3bs2DGDJUqS9onB4iSvAZYB7x61vKrOr6plVbVs4cKFs1ucJO3n5ne47VuBRa35I5u2+0lyAnAm8IKqurvDeiRJI3R5RLARWJLkmCQLgFXA+naHJE8D3g+sqKrbO6xFkjSJzoKgqnYCpwOXADcCF1bV5iRrk6xour0bOAj4RJJrkqyfZHOSpI50eWqIqtoAbBhqO6s1fUKXjy9J2r19YrBYkjQ+BoEk9ZxBIEk9ZxBIUs8ZBJLUcwaBJPWcQSBJPWcQSFLPGQSS1HMGgST1nEEgST1nEEhSzxkEktRzBoEk9ZxBIEk9ZxBIUs8ZBJLUcwaBJPWcQSBJPWcQSFLPGQSS1HMGgST1nEEgST1nEEhSzxkEktRznQZBkuVJtiTZmmTNiOXPT/LPSXYmeWWXtUiSRussCJLMA84DTgSWAicnWTrU7WvAqcBHu6pDkrRr8zvc9vHA1qraBpBkHbASuGGiQ1Xd3Cz7cYd1SJJ2octTQ0cAt7Tmtzdt05ZkdZJNSTbt2LFjRoqTJA3MicHiqjq/qpZV1bKFCxeOuxxJ2q90GQS3Aota80c2bZKkfUiXQbARWJLkmCQLgFXA+g4fT5K0BzoLgqraCZwOXALcCFxYVZuTrE2yAiDJM5NsB/4j8P4km7uqR5I0WpefGqKqNgAbhtrOak1vZHDKSJI0JnNisFiS1B2DQJJ6ziCQpJ4zCCSp5wwCSeo5g0CSes4gkKSeMwgkqecMAknqOYNAknrOIJCknjMIJKnnDAJJ6jmDQJJ6ziCQpJ4zCCSp5wwCSeo5g0CSes4gkKSeMwgkqecMAknqOYNAknrOIJCknjMIJKnnDAJJ6jmDQJJ6rtMgSLI8yZYkW5OsGbH8gCQfb5ZflWRxl/VIkh6osyBIMg84DzgRWAqcnGTpULfTgDur6ljgXOCcruqRJI3W5RHB8cDWqtpWVfcA64CVQ31WAhc00xcBv5AkHdYkSRoyv8NtHwHc0prfDjxrsj5VtTPJd4GfBb7V7pRkNbC6mb0ryZZOKp45hzH0HPZR1tmSvT8enSv7E+ZOrdbZspd/o0dPtqDLIJgxVXU+cP6465iqJJuqatm469gd65xZc6VOmDu1Wufs6PLU0K3Aotb8kU3byD5J5gM/A9zRYU2SpCFdBsFGYEmSY5IsAFYB64f6rAdOaaZfCVxWVdVhTZKkIZ2dGmrO+Z8OXALMAz5YVZuTrAU2VdV64M+AjyTZCnybQVjsD+bKaSzrnFlzpU6YO7Va5yyIb8Alqd/8ZrEk9ZxBIEk9ZxDsgSSPSHJpkq8094eO6HNckn9KsjnJdUle3Vr2oSRfTXJNczuugxr3+PIeSc5o2rckeclM1zbNOt+c5IZmH34mydGtZfe19uHwBxFmu85Tk+xo1fO61rJTmr+VryQ5ZXjdWa7z3FaNX07ynday2dyfH0xye5IvTrI8Sf6oeR7XJXl6a9ls7s/d1fmrTX3XJ/l8kqe2lt3ctF+TZFOXde61qvI2zRvwLmBNM70GOGdEn8cDS5rpxwDfAA5p5j8EvLLD+uYBNwGPBRYA1wJLh/r8BvAnzfQq4OPN9NKm/wHAMc125o2xzhcBD22m//NEnc38XbP07z2VOk8F/njEuo8AtjX3hzbTh46rzqH+b2TwIY5Z3Z/NYz0feDrwxUmWvxT4OyDAs4GrZnt/TrHO50w8PoPL6VzVWnYzcNhs7dO9uXlEsGfal8a4ADhpuENVfbmqvtJMfx24HVg4S/XtzeU9VgLrquruqvoqsLXZ3ljqrKrLq+oHzeyVDL6PMtumsj8n8xLg0qr6dlXdCVwKLN9H6jwZ+FhHtexSVX2WwScFJ7MS+HANXAkckuRwZnd/7rbOqvp8UweM7+9zrxkEe+ZRVfWNZvo24FG76pzkeAbv0G5qNf9+c0h5bpIDZri+UZf3OGKyPlW1E5i4vMdU1p3NOttOY/AuccKBSTYluTLJA8J4Bk21zlc0/6YXJZn4MuU+uT+bU2zHAJe1mmdrf07FZM9lNvfndA3/fRbwqSRXN5fJ2WfNiUtMjEOSTwOPHrHozPZMVVWSST+D27yL+QhwSlX9uGk+g0GALGDw+eO3Amtnou79VZLXAMuAF7Saj66qW5M8FrgsyfVVddPoLXTuk8DHquruJK9ncLT14jHVMhWrgIuq6r5W2760P+eUJC9iEATPbTU/t9mfjwQuTfKl5ghjn+MRwSSq6oSqetKI2/8Fvtm8wE+80N8+ahtJHg5cDJzZHN5ObPsbzSHv3cCfM/OnXvbm8h5TWXc26yTJCQwCeEWzzwCoqlub+23AFcDTxlVnVd3Rqu0DwDOmuu5s1tmyiqHTQrO4P6disucym/tzSpI8hcG/+cqq+sklclr783bgr+nuFOveG/cgxVy8Ae/m/oPF7xrRZwHwGeC3Ryw7vLkP8F7g7Bmubz6DQbRj+Omg4ROH+vwm9x8svrCZfiL3HyzeRneDxVOp82kMTqktGWo/FDigmT4M+Aq7GBidhToPb03/MnBlM/0I4KtNvYc2048YV51Nv59jMJCZcezP1mMuZvJB2Jdx/8HiL8z2/pxinUcxGEd7zlD7w4CDW9OfB5Z3WedePcdxFzAXbwzOpX+m+c/y6Yk/RAanLj7QTL8GuBe4pnU7rll2GXA98EXgL4CDOqjxpcCXmxfRM5u2tQzeVQMcCHyi+SP+AvDY1rpnNuttAU7seF/urs5PA99s7cP1Tftzmn14bXN/2pjrfCewuanncuDnWuv+erOftwK/Ns46m/m3MfTmYwz782MMPkl3L4Pz/KcBbwDe0CwPgx+2uqmpZ9mY9ufu6vwAcGfr73NT0/7YZl9e2/xdnNllnXt78xITktRzjhFIUs8ZBJLUcwaBJPWcQSBJPWcQSFLPGQSS1HMGgST1nEEg7aUkz2wuNndgkoc1v0HxpHHXJU2VXyiTZkCStzP4tvZDgO1V9c4xlyRNmUEgzYAkC4CNwI8YXHfmvt2sIu0zPDUkzYyfBQ4CDmZwZCDNGR4RSDOg+Y3fdQyu/Hl4VZ0+5pKkKfOHaaS9lOS1wL1V9dEk84DPJ3lxVV22u3WlfYFHBJLUc44RSFLPGQSS1HMGgST1nEEgST1nEEhSzxkEktRzBoEk9dz/B8ZlOnWkYsk3AAAAAElFTkSuQmCC\n",
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
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "id": "cAhjUO5FUMGw",
        "outputId": "ada5fc7e-10ec-4c91-93f8-c261d721e46e"
      },
      "source": [
        "# ③計算伯努利分配的累積機率 (cumulative density function)，pmf 的累加\n",
        "# P(X=x) --> 是機率\n",
        "cumsum_probs = stats.bernoulli.cdf(r,p)\n",
        "plt.ylabel('P(X<=x)')\n",
        "plt.xlabel('x')\n",
        "plt.title('bernoulli(p=0.4)')\n",
        "plt.plot(r, cumsum_probs)\n",
        "plt.show()"
      ],
      "execution_count": 9,
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
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8Vjs25doURvk",
        "outputId": "39e74418-eebb-4f52-c6e5-0ca7fdd76ba3"
      },
      "source": [
        "# ④ 透過 cdf ，給定一個 機率值，反推出對應到的 x\n",
        "p_loc = stats.bernoulli.ppf(cumsum_probs, p)\n",
        "print(p_loc)\n",
        "#看上圖看結果"
      ],
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[0. 1.]\n"
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
          "height": 283
        },
        "id": "WY4fCUkRUXt8",
        "outputId": "3ae4e87d-d89d-4268-b2ab-f042814ff444"
      },
      "source": [
        "# ⑤產生符合伯努利分配的隨機樣本點 (random sample)\n",
        "X = stats.bernoulli.rvs(p,size=20)\n",
        "print(X)\n",
        "plt.hist(X)\n",
        "plt.show()\n",
        "#試試看，每一次的結果一樣嗎?"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[1 0 0 0 1 0 0 0 1 0 0 1 0 1 0 0 0 1 0 0]\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXAAAAD4CAYAAAD1jb0+AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAANG0lEQVR4nO3dfYxl9V3H8fenjFhRLOhOawXWoYYSCWogE6U2abWLzQoNa2JjIEFBN05aY0VtQqgk1ug/ELU+RGLdWAQVaRWrbsRqkUI2NoDO8rhAS5GudCntDqKobRRIv/5xr2Y73Z179p4z9+7Pfb+Szd6HM/d8fzuzb86euWdIVSFJas8r5j2AJGk6BlySGmXAJalRBlySGmXAJalRC7Pc2ZYtW2ppaWmWu5Sk5u3du/e5qlpc//hMA760tMTq6uosdylJzUvyz4d73FMoktQoAy5JjTLgktQoAy5JjTLgktQoAy5JjZoY8CQ3JjmYZN9hnnt3kkqyZXPGkyQdSZcj8JuA7esfTHIG8Fbg6YFnkiR1MDHgVbUHeP4wT/06cDXgDxSXpDmY6krMJDuAZ6rqoSSTtl0BVgC2bt06ze4AWLrm9qk/tq/91108t31L0pEc9Tcxk5wE/DzwC122r6pdVbVcVcuLi19xKb8kaUrTvAvlW4EzgYeS7AdOB+5P8k1DDiZJ2thRn0KpqkeAV//v/XHEl6vquQHnkiRN0OVthLcC9wBnJzmQZOfmjyVJmmTiEXhVXTbh+aXBppEkdeaVmJLUKAMuSY0y4JLUKAMuSY0y4JLUKAMuSY0y4JLUKAMuSY0y4JLUKAMuSY0y4JLUKAMuSY0y4JLUKAMuSY0y4JLUKAMuSY0y4JLUKAMuSY0y4JLUKAMuSY3q8n+lvzHJwST7DnnsV5J8IsnDSf48ySmbO6Ykab0uR+A3AdvXPXYHcG5VfQfwBPCegeeSJE0wMeBVtQd4ft1jH62ql8d37wVO34TZJEkbGOIc+I8DHznSk0lWkqwmWV1bWxtgd5Ik6BnwJNcCLwO3HGmbqtpVVctVtby4uNhnd5KkQyxM+4FJrgTeBmyrqhpsIklSJ1MFPMl24GrgzVX1xWFHkiR10eVthLcC9wBnJzmQZCfw28DJwB1JHkzy/k2eU5K0zsQj8Kq67DAPf2ATZpEkHQWvxJSkRhlwSWqUAZekRhlwSWqUAZekRhlwSWqUAZekRhlwSWqUAZekRhlwSWqUAZekRhlwSWqUAZekRhlwSWqUAZekRhlwSWqUAZekRhlwSWqUAZekRhlwSWqUAZekRk0MeJIbkxxMsu+Qx74hyR1JPjX+/dTNHVOStF6XI/CbgO3rHrsGuLOqzgLuHN+XJM3QxIBX1R7g+XUP7wBuHt++GfjBgeeSJE0w7Tnw11TVs+PbnwNec6QNk6wkWU2yura2NuXuJEnr9f4mZlUVUBs8v6uqlqtqeXFxse/uJElj0wb880leCzD+/eBwI0mSupg24LuBK8a3rwD+cphxJElddXkb4a3APcDZSQ4k2QlcB3x/kk8BF47vS5JmaGHSBlV12RGe2jbwLJKko+CVmJLUKAMuSY0y4JLUKAMuSY0y4JLUKAMuSY0y4JLUKAMuSY0y4JLUKAMuSY0y4JLUKAMuSY0y4JLUKAMuSY0y4JLUKAMuSY0y4JLUKAMuSY0y4JLUKAMuSY3qFfAkP5vk0ST7ktya5JVDDSZJ2tjUAU9yGvDTwHJVnQucAFw61GCSpI31PYWyAHxNkgXgJOCz/UeSJHUxdcCr6hngV4GngWeBF6rqo+u3S7KSZDXJ6tra2vSTSpK+TJ9TKKcCO4AzgW8GvjbJ5eu3q6pdVbVcVcuLi4vTTypJ+jJ9TqFcCHy6qtaq6iXgw8D3DDOWJGmSPgF/GrggyUlJAmwDHh9mLEnSJH3Ogd8H3AbcDzwyfq1dA80lSZpgoc8HV9V7gfcONIsk6Sh4JaYkNcqAS1KjDLgkNcqAS1KjDLgkNcqAS1KjDLgkNcqAS1KjDLgkNcqAS1KjDLgkNcqAS1KjDLgkNcqAS1KjDLgkNcqAS1KjDLgkNcqAS1KjDLgkNcqAS1KjDLgkNapXwJOckuS2JJ9I8niSNww1mCRpYws9P/43gb+pqrcnORE4aYCZJEkdTB3wJK8C3gRcCVBVLwIvDjOWJGmSPkfgZwJrwO8n+U5gL3BVVX3h0I2SrAArAFu3bu2xO0nqZ+ma2+e27/3XXTz4a/Y5B74AnA/8TlWdB3wBuGb9RlW1q6qWq2p5cXGxx+4kSYfqE/ADwIGqum98/zZGQZckzcDUAa+qzwGfSXL2+KFtwGODTCVJmqjvu1DeBdwyfgfKU8CP9R9JktRFr4BX1YPA8kCzSJKOgldiSlKjDLgkNcqAS1KjDLgkNcqAS1KjDLgkNcqAS1KjDLgkNcqAS1KjDLgkNcqAS1KjDLgkNcqAS1KjDLgkNcqAS1KjDLgkNcqAS1KjDLgkNcqAS1KjDLgkNap3wJOckOSBJH81xECSpG6GOAK/Cnh8gNeRJB2FXgFPcjpwMfB7w4wjSeqq7xH4bwBXA18aYBZJ0lGYOuBJ3gYcrKq9E7ZbSbKaZHVtbW3a3UmS1ulzBP5G4JIk+4EPAm9J8kfrN6qqXVW1XFXLi4uLPXYnSTrU1AGvqvdU1elVtQRcCnysqi4fbDJJ0oZ8H7gkNWphiBepqruBu4d4LUlSNx6BS1KjDLgkNcqAS1KjDLgkNcqAS1KjDLgkNcqAS1KjDLgkNcqAS1KjDLgkNcqAS1KjDLgkNcqAS1KjDLgkNcqAS1KjDLgkNcqAS1KjDLgkNcqAS1KjDLgkNcqAS1Kjpg54kjOS3JXksSSPJrlqyMEkSRtb6PGxLwPvrqr7k5wM7E1yR1U9NtBskqQNTH0EXlXPVtX949v/ATwOnDbUYJKkjQ1yDjzJEnAecN9hnltJsppkdW1tbYjdSZIYIOBJvg74M+Bnqurf1z9fVbuqarmqlhcXF/vuTpI01ivgSb6KUbxvqaoPDzOSJKmLPu9CCfAB4PGqet9wI0mSuuhzBP5G4EeAtyR5cPzrooHmkiRNMPXbCKvq74EMOIsk6Sh4JaYkNcqAS1KjDLgkNcqAS1KjDLgkNcqAS1KjDLgkNcqAS1KjDLgkNcqAS1KjDLgkNcqAS1KjDLgkNcqAS1KjDLgkNcqAS1KjDLgkNcqAS1KjDLgkNcqAS1KjDLgkNapXwJNsT/LJJE8muWaooSRJk00d8CQnADcAPwCcA1yW5JyhBpMkbazPEfh3AU9W1VNV9SLwQWDHMGNJkiZZ6PGxpwGfOeT+AeC712+UZAVYGd/9zySfnHJ/W4DnpvzYXnL9PPYKzHHNc+Sajw/H3Zpzfa81f8vhHuwT8E6qahewq+/rJFmtquUBRmqGaz4+uObjw2asuc8plGeAMw65f/r4MUnSDPQJ+D8CZyU5M8mJwKXA7mHGkiRNMvUplKp6OclPAX8LnADcWFWPDjbZV+p9GqZBrvn44JqPD4OvOVU19GtKkmbAKzElqVEGXJIadcwFfNLl+Um+OsmHxs/fl2Rp9lMOq8Oafy7JY0keTnJnksO+J7QlXX8MQ5IfSlJJmn7LWZf1Jvnh8ef50SR/POsZh9bh63prkruSPDD+2r5oHnMOKcmNSQ4m2XeE55Pkt8Z/Jg8nOb/XDqvqmPnF6Juh/wS8DjgReAg4Z902Pwm8f3z7UuBD8557Bmv+PuCk8e13Hg9rHm93MrAHuBdYnvfcm/w5Pgt4ADh1fP/V8557BmveBbxzfPscYP+85x5g3W8Czgf2HeH5i4CPAAEuAO7rs79j7Qi8y+X5O4Cbx7dvA7YlyQxnHNrENVfVXVX1xfHdexm9575lXX8Mwy8D1wP/NcvhNkGX9f4EcENV/StAVR2c8YxD67LmAr5+fPtVwGdnON+mqKo9wPMbbLID+IMauRc4Jclrp93fsRbww12ef9qRtqmql4EXgG+cyXSbo8uaD7WT0X/BWzZxzeN/Wp5RVbfPcrBN0uVz/Hrg9Uk+nuTeJNtnNt3m6LLmXwQuT3IA+GvgXbMZba6O9u/7hjb9UnoNJ8nlwDLw5nnPspmSvAJ4H3DlnEeZpQVGp1G+l9G/sPYk+faq+re5TrW5LgNuqqpfS/IG4A+TnFtVX5r3YK041o7Au1ye/3/bJFlg9E+vf5nJdJuj048kSHIhcC1wSVX994xm2yyT1nwycC5wd5L9jM4V7m74G5ldPscHgN1V9VJVfRp4glHQW9VlzTuBPwGoqnuAVzL6IVf/nw36I0iOtYB3uTx/N3DF+PbbgY/V+LsDjZq45iTnAb/LKN6tnxuFCWuuqheqaktVLVXVEqPz/pdU1ep8xu2ty9f1XzA6+ibJFkanVJ6a5ZAD67Lmp4FtAEm+jVHA12Y65eztBn50/G6UC4AXqurZqV9t3t+1PcJ3aZ9g9B3sa8eP/RKjv8Aw+iT/KfAk8A/A6+Y98wzW/HfA54EHx792z3vmzV7zum3vpuF3oXT8HIfRaaPHgEeAS+c98wzWfA7wcUbvUHkQeOu8Zx5gzbcCzwIvMfpX1U7gHcA7Dvk83zD+M3mk79e1l9JLUqOOtVMokqSODLgkNcqAS1KjDLgkNcqAS1KjDLgkNcqAS1Kj/gdauk2ZamdxnQAAAABJRU5ErkJggg==\n",
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
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OF_RWWkzUaXF",
        "outputId": "aab0767e-2296-41cf-a679-3a3275a5f8e2"
      },
      "source": [
        "#6.計算固定參數下，隨機變數的平均數、變異數、偏度和峰度。\n",
        "stat_ber=stats.bernoulli.stats(p,moments='mvks')\n",
        "print(stat_ber)\n",
        "print(type(stat_ber))\n",
        "#E(X)\n",
        "# 平均數\n",
        "print(\"bernoulli mean=\",float(stat_ber[0]))\n",
        "# 變異數\n",
        "print(\"bernoulli variance=\",float(stat_ber[1]))\n",
        "# 偏度\n",
        "print(\"bernoulli kurtosis=\",float(stat_ber[2]))\n",
        "# 峰度\n",
        "print(\"bernoulli skew=\",float(stat_ber[3]))"
      ],
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "(array(0.4), array(0.24), array(0.40824829), array(-1.83333333))\n",
            "<class 'tuple'>\n",
            "bernoulli mean= 0.4\n",
            "bernoulli variance= 0.24\n",
            "bernoulli kurtosis= 0.40824829046386296\n",
            "bernoulli skew= -1.8333333333333337\n"
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
          "height": 295
        },
        "id": "bJSn9nMLUvZz",
        "outputId": "c99c7d80-9e48-4a8f-ee99-0b7391bfdc2a"
      },
      "source": [
        "'''\n",
        "# 二項分佈 (binomial distribution)\n",
        "# 前提：獨立重複試驗、有放回、只有兩個結果\n",
        "# 二項分佈指出，隨機一次試驗出現事件A的機率如果為p，那麼在重複 n 次試驗中出現 x 次事件A的機率為：\n",
        "# f(n,x,p) = choose(n, x) * p**x * (1-p)**(n-x)\n",
        "'''\n",
        "# 1.定義二項分佈的基本資訊\n",
        "p = 0.5 # 事件A 機率 0.4\n",
        "n = 5  # 重複實驗5次,\n",
        "r = np.arange(0,6) # 可以出現的範圍為 0,1,2,...,5-->6種可能出現的結果\n",
        "#print(type(k))\n",
        "\n",
        "# 2.計算二項分佈的概率質量分佈 (probability mass function)\n",
        "# 之所以稱為質量，是因為離散的點\n",
        "# P(X=x) --> 是機率\n",
        "probs = stats.binom.pmf(r, n, p)\n",
        "#array([ 0.07776, 0.2592 , 0.3456 , 0.2304 , 0.0768 , 0.01024])\n",
        "plt.bar(r, probs)\n",
        "plt.ylabel('P(X=x)')\n",
        "plt.xlabel('x')\n",
        "plt.title('binomial(n=5,p=0.5)')\n",
        "plt.show()\n",
        "\n",
        "#學生額外小練習: 可以調整 p 的不同值，p接近於1 時，p=0.5, p 接近於 0時，看 pmf 的變化。"
      ],
      "execution_count": 13,
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
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "id": "Qj3fzZFgVLD9",
        "outputId": "50340563-f6be-4134-f3fe-2493ce4c3197"
      },
      "source": [
        "# 3.計算二項分佈的累積機率 (cumulative density function)，pmf 的累加\n",
        "# 之所以稱為質量，是因為離散的點，預設體積（即寬度）為1\n",
        "# P(X=x) --> 是機率\n",
        "cumsum_probs = stats.binom.cdf(r, n, p)\n",
        "#array([ 0.07776, 0.2592 , 0.3456 , 0.2304 , 0.0768 , 0.01024])\n",
        "plt.show()\n",
        "plt.ylabel('P(X<=x)')\n",
        "plt.xlabel('x')\n",
        "plt.title('binomial(n=5,p=0.4)')\n",
        "plt.plot(r, cumsum_probs)\n",
        "plt.show()"
      ],
      "execution_count": 14,
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
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gOP9jJYgVQ6Y",
        "outputId": "2ab791c5-fc1b-460c-ba7d-eda2bfbdfaea"
      },
      "source": [
        "# 4.透過 cdf ，給定一個 機率值，反推出對應到的 x\n",
        "p_loc= stats.binom.ppf(cumsum_probs, n, p)\n",
        "print(p_loc)\n",
        "#看上圖看結果"
      ],
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[0. 1. 2. 3. 4. 5.]\n"
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
          "height": 283
        },
        "id": "F_FWlSAdVTSf",
        "outputId": "4fd251a4-7e93-4b11-9c7d-0cc275b9463c"
      },
      "source": [
        "# 5.產生符合二項分佈的隨機樣本點 (random sample)\n",
        "X = stats.binom.rvs(n,p,size=20)\n",
        "#array([2, 3, 1, 2, 2, 2, 1, 2, 2, 3, 3, 0, 1, 1, 1, 2, 3, 4, 0, 3])\n",
        "print(X)\n",
        "plt.hist(X)\n",
        "plt.show()\n",
        "#試試看，，每一次的結果一樣嗎?"
      ],
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[4 4 3 3 3 4 2 4 3 3 2 2 4 2 2 3 3 4 3 4]\n"
          ],
          "name": "stdout"
        },
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
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "d33EzWZ4VWSM",
        "outputId": "a0cde978-c4b3-47f3-c82c-a7b077a2a3cd"
      },
      "source": [
        "#6.計算固定參數下，隨機變數的平均數、變異數、偏度和峰度。\n",
        "stat_bin=stats.binom.stats(n,p,moments='mvks')\n",
        "print(stat_bin)\n",
        "print(type(stat_bin))\n",
        "#E(X)\n",
        "print(\"binomial mean=\",float(stat_bin[0]))\n",
        "print(\"binomial variance=\",float(stat_bin[1]))\n",
        "print(\"binomial kurtosis=\",float(stat_bin[2]))\n",
        "print(\"binomial skew=\",float(stat_bin[3]))"
      ],
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "(array(2.5), array(1.25), array(0.), array(-0.4))\n",
            "<class 'tuple'>\n",
            "binomial mean= 2.5\n",
            "binomial variance= 1.25\n",
            "binomial kurtosis= 0.0\n",
            "binomial skew= -0.4\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QkkC4W_EVoaB"
      },
      "source": [
        "# 機率可以怎麼用？\n",
        "# 丟一個銅板，丟了100次，出現正面 50 次的機率有多大。\n",
        "# (提示：先想是哪一種分配，然後透過 python 語法進行計算)\n"
      ],
      "execution_count": 18,
      "outputs": []
    }
  ]
}