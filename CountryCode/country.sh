json_file="data.json"

for iso_alpha2 in "$@"; do
    name=$(jq -r ".data[\"$iso_alpha2\"].name" "$json_file")
    echo "$iso_alpha2: $name"
done