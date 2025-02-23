
{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "sesi6.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyPFMdvC8/vKAFXoxGe1j5XC",
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
        "<a href=\"https://colab.research.google.com/github/hendriahm/python/blob/master/sesi6.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "qTjxc14t23Ha",
        "colab_type": "text"
      },
      "source": [
        "**Program Sederhana Membuat Tuple**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "F6_EVThE20TC",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# Deklarasi variabel stup1, stup2 dan stup3\n",
        "stup1 = ('bahasa arab', 'bahasa aceh', 2019, 2020)\n",
        "stup2 = (1, 2, 3, 4, 5, 6, 7, 8)\n",
        "stup3 = \"e\", \"f\", \"g\", \"h\"\n",
        "\n",
        "# Mengakses nilai pada variabel ketiga tupel diatas\n",
        "print (\"stup1[1]: \", stup1[1])\n",
        "print (\"stup2[1:5]: \", stup2[1:5])"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "9e5UgsZy4glk",
        "colab_type": "text"
      },
      "source": [
        "**Mengakses Nilai Tuple**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "H35GakMK5MO8",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# Deklarasi Variabel ach\n",
        "ach = (\"Mie Aceh\", 10000, 3.5, True, 'AyamPramugari', 88j)\n",
        "\n",
        "# Mengakses nilai tuple  \n",
        "# Data pertama indeks 0\n",
        "print(\"ach[0]:\", ach[0])\n",
        "# Data kedua indeks 1\n",
        "print(\"ach[1]:\", ach[1])\n",
        "# Data ketiga indeks 2\n",
        "print(\"ach[2]:\", ach[2])\n",
        "# Data antara indeks 2 dan 5\n",
        "print(\"ach[2:5]:\", ach[2:5])\n",
        "# Data dari indeks satu sampai indeks 3\n",
        "print(\"ach[:3]:\", ach[:3])\n",
        "# Data dari indeks 3 sampai dengan indeks seterusnya\n",
        "print(\"ach[3:]:\", ach[3:])\n",
        "# Data keseluruhan\n",
        "print(\"ach[:]:\", ach[:])"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "_fX8pSaaXULb",
        "colab_type": "text"
      },
      "source": [
        "**Membuat Tuple dari Kumpulan Tuple**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Yq0upGZW4lJ0",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# Contoh menambah variabel baru pada daftar tuple\n",
        "stup1 = (10, 5.78)\n",
        "stup2 = ('def', 'opq')\n",
        "\n",
        "# Jika ditambah baris berikut:\n",
        "# stup1[0] = 100;\n",
        "# tidak bisa dilakukan pada tuple python\n",
        "\n",
        "# Jadi, buatlah variabel tuple baru sebagai berikut\n",
        "stup3 = stup1 + stup2\n",
        "print (stup3)\n",
        "\n",
        "del stup3:\n",
        "print(\"setelah dihapus:\")"
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}
