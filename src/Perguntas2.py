{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO9RVxJxqch+V9s9/Kwy+nF"
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
      "cell_type": "code",
      "source": [
        "def valores_nao_aceitos(valor_escolhido, valores_aceitos):\n",
        "  if valor_escolhido not in valores_aceitos:\n",
        "    print(\"Valor não aceito \\n\")\n",
        "    return False\n",
        "  else:\n",
        "    return True\n",
        "\n",
        "\n",
        "def perguntas_usuario():\n",
        "  aceito_1 = False\n",
        "  aceito_2 = False\n",
        "  aceito_3 = False\n",
        "  aceito_4 = False\n",
        "\n",
        "  while aceito_1 == False:\n",
        "    variaveis_dict = {\n",
        "        \"1\": \"Velocidade\",\n",
        "        \"2\": \"Temperatura\",\n",
        "        \"3\": \"Ambos\"\n",
        "    }\n",
        "\n",
        "    variavel = input(\n",
        "        '''Qual variável deseja observar? \\n\n",
        "        1 - Velocidade \\n\n",
        "        2 - Temperatura \\n\n",
        "        3 - Ambos \\n \\n'''\n",
        "        )\n",
        "\n",
        "    print(\"\\n\")\n",
        "\n",
        "    aceito_1 = valores_nao_aceitos(variavel, [\"1\", \"2\", \"3\"])\n",
        "\n",
        "\n",
        "  if variavel in ['1', '2']:\n",
        "\n",
        "    while aceito_2 == False:\n",
        "      modo_dict = {\n",
        "          \"1\": \"Original\",\n",
        "          \"2\": \"Original-Derivada\"\n",
        "      }\n",
        "\n",
        "      modo = input(\n",
        "        '''Qual modo deseja observar? \\n\n",
        "        1 - Original \\n\n",
        "        2 - Original-Derivada \\n \\n'''\n",
        "      )\n",
        "\n",
        "      print(\"\\n\")\n",
        "\n",
        "      aceito_2 = valores_nao_aceitos(modo, [\"1\", \"2\"])\n",
        "\n",
        "\n",
        "    if variavel == '1':\n",
        "\n",
        "      while aceito_3 == False:\n",
        "        componente_dict = {\n",
        "            \"1\": \"Resultante\",\n",
        "            \"2\": \"u\",\n",
        "            \"3\": \"v\"\n",
        "        }\n",
        "\n",
        "        componente = input(\n",
        "          '''Qual componente deseja observar? \\n\n",
        "          1 - Resultante \\n\n",
        "          2 - u \\n\n",
        "          3 - v \\n \\n'''\n",
        "        )\n",
        "\n",
        "        print(\"\\n\")\n",
        "\n",
        "        aceito_3 = valores_nao_aceitos(componente, [\"1\", \"2\", \"3\"])\n",
        "\n",
        "  while aceito_4 == False:\n",
        "    plataformas_dict = {\n",
        "        \"p1\": 'NAMORADO 2 (PNA-2)',\n",
        "        \"p2\": 'PETROBRAS 26 (P-26)',\n",
        "        \"p3\": 'PETROBRAS 32 (P-32)',\n",
        "        \"p4\": 'PETROBRAS 37 (P-37)',\n",
        "        \"p5\": 'PETROBRAS IX',\n",
        "        \"p6\": 'PETROBRAS XIX',\n",
        "        \"p7\": 'PETROBRAS XXXIII',\n",
        "        \"p8\": 'VERMELHO 1 (PVM-1)',\n",
        "        \"p9\": 'VERMELHO 2 (PVM-2)'\n",
        "\n",
        "    }\n",
        "    plataforma = input(\n",
        "      '''Qual plataforma deseja observar? \\n\n",
        "      p1 - NAMORADO 2 (PNA-2) \\n\n",
        "      p2 - PETROBRAS 26 (P-26) \\n\n",
        "      p3 - PETROBRAS 32 (P-32) \\n\n",
        "      p4 - PETROBRAS 37 (P-37) \\n\n",
        "      p5 - PETROBRAS IX \\n\n",
        "      p6 - PETROBRAS XIX \\n\n",
        "      p7 - PETROBRAS XXXIII \\n\n",
        "      p8 - VERMELHO 1 (PVM-1) \\n\n",
        "      p9 - VERMELHO 2 (PVM-2) \\n \\n'''\n",
        "    )\n",
        "\n",
        "    print(\"\\n\")\n",
        "\n",
        "    aceito_4 = valores_nao_aceitos(plataforma, [\"p1\", \"p2\", \"p3\", \"p4\", \"p5\", \"p6\", \"p7\", \"p8\", \"p9\"])\n",
        "\n",
        "\n",
        "\n",
        "  variavel = variaveis_dict[variavel]\n",
        "  modo = modo_dict[modo]\n",
        "  componente = componente_dict[componente]\n",
        "  plataforma = plataformas_dict[plataforma]\n",
        "\n",
        "  argumentos = dict(\n",
        "      variavel = variavel,\n",
        "      modo = modo,\n",
        "      componente = componente,\n",
        "      plataforma = plataforma\n",
        "  )\n",
        "\n",
        "  return argumentos\n",
        "\n"
      ],
      "metadata": {
        "id": "RKlN8LUVl9_X"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}