# go.py
from ansible.module_utils.basic import AnsibleModule
from out import terraform_project

def main():
    module = AnsibleModule(
        argument_spec=dict(
            action=dict(type='str', required=False, default="list")
        )
    )

    action = module.params['action']
    result = {"changed": False, "action": action}

    try:
        if action == "list":
            output = terraform_project.ManageProject()
            result["changed"] = True
            result["message"] = "Projects listed successfully"
            result["output"] = output
        else:
            module.fail_json(msg=f"Invalid action: {action}. Only 'list' is supported.", **result)

        module.exit_json(**result)

    except Exception as e:
        module.fail_json(msg=str(e), **result)

if __name__ == '__main__':
    main()
