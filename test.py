x = [
        "\n\t\t\t\t\t\t\t\t",
        "Traffik Kitchen and Cocktails",
        "\n\t\t\t\t\t\t\t\t\t",
        "1100 Crescent Avenue Northeast ",
        "\n\t\t\t\t\t\t\t\t\t",
        "Atlanta, GA 30309 ",
        "\n\t\t\t\t\t\t\t\t",
        "\n\t\t\t\t\t\t\t\t\t",
        "View Map",
        "\n\t\t\t\t\t\t\t\t\t",
        "View Map",
        "\n\t\t\t\t\t\t\t\t",
        "\n\t\t\t\t\t\t\t"
    ]

new_list = [item for item in x if '\n' not in item and '\t' not in item]
print(new_list)

