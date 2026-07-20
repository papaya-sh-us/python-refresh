def read_config(filename):
    settings = {}
    try:
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
    except FileNotFoundError:
        print("Error: file not found")
        return {}
    else:
        for line in lines:
            line = line.strip()
            if line == "":
                continue
            key, value = line.split("=")
            settings[key] = value
        print(f"Loaded {len(settings)} settings")
        return settings
    finally:
        print("Config read attempted")


with open("config.txt", "w") as f:
    f.write("name=Jeffrey\n")
    f.write("age=30\n")
    f.write("color=blue\n")

print(read_config("config.txt"))

print(read_config("missing.txt"))