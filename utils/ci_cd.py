import os
import yaml

def trigger_pipeline(version):
    workflow = {
        "name": f"Deploy v{version}",
        "on": {"workflow_dispatch": {}},
        "jobs": {
            "deploy": {
                "runs-on": "ubuntu-latest",
                "steps": [
                    {"uses": "actions/checkout@v4"},
                    {"name": "Deploy", "run": f"echo 'Deploying {version}'"}
                ]
            }
        }
    }
    
    with open("workflows/deploy.yml", "w") as f:
        yaml.dump(workflow, f)