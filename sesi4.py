{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Sesi4.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyNM3X9jxrHmuHcwYqO7flpY",
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
        "<a href=\"https://colab.research.google.com/github/hendriahm/python/blob/master/Sesi4.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ISC17aODVlDI",
        "colab_type": "text"
      },
      "source": [
        "**Membuat fungsi tanpa parameter**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "KLjnozP9TTUt",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# Deklarasi fungsi salam_olahraga\n",
        "def salam_olahraga():\n",
        "    # Mencetak ouput pada fungsi salam_olahraga\n",
        "    print (\"JANGAN LUPA OLAHRAGA HARI INI!\")\n",
        "\n",
        "# Memanggil fungsi salam_olahraga\n",
        "salam_olahraga()  # memanggil fungsi salam_olahraga\n",
        "salam_olahraga()  # fungsi salam_olahraga dipanggil lagi"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "mCF3HuJnW67r",
        "colab_type": "text"
      },
      "source": [
        "**Membuat fungsi dengan Parameter**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "dXKqSU5AW_ot",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# Program Fungsi dengan parameter \n",
        "# Fungsi untuk menyapa seseorang sesuai nama yang dimasukkan sebagai parameter \n",
        "def kenalan(nama): \n",
        "     print(\"Salam, \" + nama + \". Apa kabar?\") \n",
        "\n",
        "# pemanggilan fungsi \n",
        "kenalan('Hamzah') "
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Ir-wbgYVu4HH",
        "colab_type": "text"
      },
      "source": [
        "**Program untuk mencari nilai median**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ogehUKpLu8Nm",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# Menghitung dan menampilkan nilai median dari inputan tiga angka\n",
        "# Program ini dibuat dengan kata kunci def untuk membuat fungsi\n",
        "# menghitung nilai median dari 3 nilai yang diinput\n",
        "\n",
        "def median(a, b, c):\n",
        "# Proses perhitungan median cara pertama dengan perbandingan\n",
        "# Menggunakan kata kunci retun untuk mengembalikan nilai\n",
        "# untuk masing-masing nilai, yaitu a, b dan c\n",
        "  if a < b and b < c or a> b and b > c:\n",
        "    return b\n",
        "  if b < a and a < c or b > a and a > c:\n",
        "    return a\n",
        "  if c < a and b < c or c > a and b > c:\n",
        "    return c\n",
        "\n",
        "# Proses perhitungan median cara kedua\n",
        "def median2(a, b, c):\n",
        "    return a + b + c - min(a, b, c) - max(a, b, c)\n",
        "\n",
        "# Menampilkan nilai inputan 3 angka\n",
        "def utama():\n",
        "  x = float(input(\"Masukkan nilai pertama:\"))\n",
        "  y = float(input(\"Masukkan nilai kedua:\"))\n",
        "  z = float(input(\"Masukkan nilai ketiga:\"))\n",
        "\n",
        "  print(\"Nilai median dengan cara pertama:\", median(x, y, z))\n",
        "  print(\"Nilai median dengan cara kedua:\", median2(x, y, z))\n",
        "\n",
        "# Memanggil fungsi utama()\n",
        "utama()"
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}