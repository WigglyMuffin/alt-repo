import json
import sys
import urllib.request

SOURCE_URL = "https://raw.githubusercontent.com/WigglyMuffin/DalamudPlugins/main/pluginmaster.json"
SOURCE_INTERNAL_NAME = "Questionable"
ALIAS_INTERNAL_NAME = "QuestionablePlus"
ALIAS_NAME_SUFFIX = " Plus"
OUTPUT_FILE = "pluginmaster.json"


def main():
    print(f"Fetching {SOURCE_URL}")
    with urllib.request.urlopen(SOURCE_URL) as resp:
        plugins = json.loads(resp.read().decode("utf-8"))

    source = None
    for plugin in plugins:
        if plugin.get("InternalName") == SOURCE_INTERNAL_NAME:
            source = plugin
            break

    if not source:
        print(f"Could not find {SOURCE_INTERNAL_NAME} in source pluginmaster.json")
        sys.exit(1)

    source["InternalName"] = ALIAS_INTERNAL_NAME
    source["Name"] = source.get("Name", SOURCE_INTERNAL_NAME) + ALIAS_NAME_SUFFIX

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump([source], f, indent=4, ensure_ascii=False, sort_keys=True)

    print(f"Wrote {OUTPUT_FILE}: {ALIAS_INTERNAL_NAME} v{source.get('AssemblyVersion')} API{source.get('DalamudApiLevel')}")


if __name__ == "__main__":
    main()
