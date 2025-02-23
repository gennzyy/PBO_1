
{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "sesi5.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyNrFXtDZjM2d62KpkuyxDve",
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
        "<a href=\"https://colab.research.google.com/github/hendriahm/python/blob/master/sesi5.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "2HJ7cUMhuNSF",
        "colab_type": "text"
      },
      "source": [
        "**Program Membuat List**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "59I2hs4QqfCE",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# Pembuatan list pada bahasa pemrograman python\n",
        "list1 = [\"a\", \"b\", \"c\", \"d\"]\n",
        "list2 = ['bahasa arab', 'bahasa aceh', 2019, 2020]\n",
        "list3 = [1, 2, 3, 4, 5, 6, 7 ]\n",
        "\n",
        "\n",
        "# Mengakses Nilai list dalam Python\n",
        "print (\"list1[0]: \", list1[0])\n",
        "print (\"list2[1:3]: \", list2[1:3])\n",
        "print (\"list3[1:5]: \", list3[1:6])"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ePzepubIw6G_",
        "colab_type": "text"
      },
      "source": [
        "**Mengupdate Nilai pada List**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Ef3FQ2Nnw9Pj",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# Pembuatan list dan mengakses nilai list pada indeks 2\n",
        "ist = ['bahasa arab', 'bahasa aceh', 2019, 2020]\n",
        "print (\"Nilai ada pada index 2 adalah: \", list[2])\n",
        "\n",
        "# Proses Update nilai list pada indeks 2\n",
        "list[2] = 2018\n",
        "print (\"Nilai baru ada pada index 2 adalah: \", list[2])"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ztC0UcO7zsyw",
        "colab_type": "text"
      },
      "source": [
        "**Menghapus Nilai pada List**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "aT7iJAdvz0FX",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# Pembuatan list\n",
        "list = ['bahasa arab', 'bahasa aceh', 2019, 2020]\n",
        "print (\"Daftar list sebelum dihapus:\", list)\n",
        "\n",
        "# Proses menghapus nilai List pada indeks 1\n",
        "del list[1]\n",
        "print (\"Setelah dihapus nilai pada index 1 : \", list)"
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}
