{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "sesi1.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNfMQVVW44gJnT9/FOLAXfh",
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
        "<a href=\"https://colab.research.google.com/github/hendriahm/python/blob/master/sesi1.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "GiSc_8aXHQSf",
        "colab_type": "text"
      },
      "source": [
        "Menggunakan sintaks print"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "x8gH7SdYHa8M",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 119
        },
        "outputId": "43d9444f-875f-478f-897f-85bd834b2f9d"
      },
      "source": [
        "##\n",
        "# Menampilkan alamat lengkap seseorang \n",
        "#\n",
        "print(\"Hendri Ahmadian\")\n",
        "print(\"Department of Information Technology\")\n",
        "print(\"UIN Ar-Raniry\")\n",
        "print(\"Jalan Syech Abdurrauf Kopelma Darussalam\")\n",
        "print(\"Banda Aceh 23111\")\n",
        "print(\"Indonesia\")"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Hendri Ahmadian\n",
            "Department of Information Technology\n",
            "UIN Ar-Raniry\n",
            "Jalan Syech Abdurrauf Kopelma Darussalam\n",
            "Banda Aceh 23111\n",
            "Indonesia\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7tiu0HF_IRoo",
        "colab_type": "text"
      },
      "source": [
        "Menghitung luas kamar"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "uYw5THVfIV86",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 68
        },
        "outputId": "294ed012-3c85-48e8-e10f-e54b0f0313a9"
      },
      "source": [
        "##\n",
        "# Menghitung luas kamar\n",
        "#\n",
        "\n",
        "# Membaca angka yang dimasukkan oleh user\n",
        "panjang = float(input(\"Masukkan ukuran panjang dalam satuan meter \"))\n",
        "lebar = float(input(\"Masukkan ukuran lebar dalam satuan meter \"))\n",
        "\n",
        "# Proses perhitungan luas\n",
        "luas = panjang * lebar\n",
        "\n",
        "# Tampilkan hasil\n",
        "print(\"Luas dari kamar ini adalah\", luas, \"meter kuadrat\")\n"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Masukkan ukuran panjang dalam satuan meter 5\n",
            "Masukkan ukuran lebar dalam satuan meter 4\n",
            "Luas dari kamar ini adalah 20.0 meter kuadrat\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "trRLS1YcKshT",
        "colab_type": "text"
      },
      "source": [
        "Menghitung jumlah dari suatu bilangan"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RYfwo6chK1HJ",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "##\n",
        "# Menghitung jumlah dari bilangan positif pertama\n",
        "#\n",
        "\n",
        "# Membaca angka yang dimasukkan oleh user\n",
        "n = int(input(\"Masukkan bilangan bulat positif:\"))\n",
        "\n",
        "# Proses Menghitung jumlah\n",
        "sm = n * (n+1) / 2\n",
        "\n",
        "# Tampilkan hasil\n",
        "print(\"Jumlah pertama dari \", n, \"bilangan positif adalah\", sm)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "k7tQ6AlASXqA",
        "colab_type": "text"
      },
      "source": [
        "Mengenal fungsi aritmatika"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "TXs5C5EnSW7r",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 170
        },
        "outputId": "8175f913-d6ed-4be9-aec6-2c629074d826"
      },
      "source": [
        "## \n",
        "# Pengenalan operator matematika pada Python dan modul math\n",
        "#\n",
        "\n",
        "from math import log10\n",
        "\n",
        "# Membaca input dari user\n",
        "x = int (input(\"Masukkan bilangan dari x:\"))\n",
        "y = int (input(\"Masukkan bilangan dari y:\"))\n",
        "\n",
        "# Menghitung dan menampilkan operator matematika\n",
        "print(x, \"+\", y, \"adalah\", x + y)\n",
        "print(x, \"-\", y, \"adalah\", x - y)\n",
        "print(x, \"*\", y, \"adalah\", x * y)\n",
        "print(x, \"/\", y, \"adalah\", x / y)\n",
        "print(x, \"%\", y, \"adalah\", x % y)\n",
        "\n",
        "# Menghitung logaritma dan pangkat\n",
        "print(\"Logaritma basis 10 dari\", x, \"adalah\", log10(x))\n",
        "print(x, \"^\", y, \"adalah\", x**y)\n"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Masukkan bilangan dari x:2\n",
            "Masukkan bilangan dari y:3\n",
            "2 + 3 adalah 5\n",
            "2 - 3 adalah -1\n",
            "2 * 3 adalah 6\n",
            "2 / 3 adalah 0.6666666666666666\n",
            "2 % 3 adalah 2\n",
            "Logaritma basis 10 dari 2 adalah 0.3010299956639812\n",
            "2 ^ 3 adalah 8\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}