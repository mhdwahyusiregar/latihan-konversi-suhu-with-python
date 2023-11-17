def kelvin_to_celsius(kelvin):
    """
    Mengkonversi suhu dari kelvin ke celcius.

    Parameters:
    - kelvin (float): Suhu dalam kelvin.

    Returns:
    - float: Suhu dalam celcius.
    """
    return kelvin - 273.15


def celsius_to_kelvin(celsius):
    """
    Mengkonversi suhu dari celcius ke kelvin.

    Parameters:
    - celsius (float): Suhu dalam celcius.

    Returns:
    - float: Suhu dalam kelvin.
    """
    return celsius + 273.15


def convert_to_fahrenheit(suhu, unit):
    """
    Mengkonversi suhu ke fahrenheit.

    Parameters:
    - suhu (float): Suhu yang akan dikonversi.
    - unit (str): Satuan suhu, bisa "celcius" atau "kelvin".

    Returns:
    - float: Suhu dalam fahrenheit.
    """
    if unit.lower() == "celcius":
        # Jika suhu dalam celcius, konversi ke kelvin terlebih dahulu
        suhu_kelvin = celsius_to_kelvin(suhu)
    elif unit.lower() == "kelvin":
        # Jika suhu dalam kelvin, gunakan langsung
        suhu_kelvin = suhu
    else:
        # Jika unit tidak valid, raise exception
        raise ValueError("Unit yang valid adalah 'celcius' atau 'kelvin'")

    # Konversi ke fahrenheit
    suhu_fahrenheit = (suhu_kelvin - 273.15) * 9/5 + 32
    return suhu_fahrenheit


def convert_fahrenheit_to(suhu, unit):
    """
    Mengkonversi suhu dari fahrenheit.

    Parameters:
    - suhu (float): Suhu dalam fahrenheit.
    - unit (str): Satuan suhu, bisa "celcius" atau "kelvin".

    Returns:
    - float: Suhu dalam unit yang diinginkan.
    """
    # Konversi fahrenheit ke celcius terlebih dahulu
    suhu_celsius = (suhu - 32) * 5/9

    if unit.lower() == "celcius":
        return suhu_celsius
    elif unit.lower() == "kelvin":
        # Konversi suhu celcius ke kelvin
        return celsius_to_kelvin(suhu_celsius)
    else:
        # Jika unit tidak valid, raise exception
        raise ValueError("Unit yang valid adalah 'celcius' atau 'kelvin'")


# Contoh penggunaan
suhu_kelvin = 300.0
suhu_celsius = kelvin_to_celsius(suhu_kelvin)
print(f"{suhu_kelvin} Kelvin sama dengan {suhu_celsius:.2f} Celcius")

suhu_celsius = 25.0
suhu_fahrenheit = convert_to_fahrenheit(suhu_celsius, "celcius")
print(f"{suhu_celsius} Celcius sama dengan {suhu_fahrenheit:.2f} Fahrenheit")

suhu_fahrenheit = 77.0
suhu_kelvin = convert_fahrenheit_to(suhu_fahrenheit, "kelvin")
print(f"{suhu_fahrenheit} Fahrenheit sama dengan {suhu_kelvin:.2f} Kelvin")
