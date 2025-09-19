import json
from datetime import datetime
import sys

def sort_json_by_created_at(input_file, output_file=None):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Sort by wf_detais['createdAt'] in descending order
    sorted_data = sorted(
        data,
        key=lambda x: datetime.fromisoformat(x['wf_detais']['createdAt'].replace('Z', '+00:00')),
        reverse=True
    )

    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(sorted_data, f, ensure_ascii=False, indent=2)
    else:
        print(json.dumps(sorted_data, ensure_ascii=False, indent=2))

    return sorted_data

def remove_workflows_older_than(workflows, cutoff_date_str):
    """
    Remove workflows whose wf_detais['createdAt'] is older than cutoff_date_str (ISO format).
    Returns a new list.
    """
    cutoff_date = datetime.fromisoformat(cutoff_date_str.replace('Z', '+00:00'))
    filtered = [w for w in workflows if datetime.fromisoformat(w['wf_detais']['createdAt'].replace('Z', '+00:00')) >= cutoff_date]
    return filtered

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python sort_workflows.py <input_json_file> <cutoff_date_iso> [output_json_file]")
        sys.exit(1)
    input_file = sys.argv[1]
    cutoff_date_str = sys.argv[2]
    output_file = sys.argv[3] if len(sys.argv) > 3 else None
    sorted_data = sort_json_by_created_at(input_file)
    filtered_data = remove_workflows_older_than(sorted_data, cutoff_date_str)
    result_json = json.dumps(filtered_data, ensure_ascii=False, indent=2)
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result_json)
    else:
        # For Java interop, print the result to stdout
        print(result_json)
