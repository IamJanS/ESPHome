# Git Hooks for Automating Tasks

This directory contains custom Git hooks used in the repository to automate specific tasks. The hooks are configured to ensure consistency and streamline workflows.

## Pre-Push Hook

The `pre-push` hook in this directory is designed to automatically update the `README.md` file in the root of the repository before pushing changes to the remote repository. This ensures that the device table in the `README.md` is always up-to-date.

### How It Works

1. **Location**: The `pre-push` hook is located in `scripts/git-hooks/pre-push`.
2. **Execution**: When you attempt to push changes, the `pre-push` hook runs the `update_device_table.py` script.
3. **Script Functionality**:
   - The script updates the device table in the `README.md` file based on the YAML files in the repository.
   - If changes are made to the `README.md`, the hook stages and commits the updated file automatically.
4. **Configuration**: The repository is configured to use this custom hooks directory by setting the `core.hooksPath` Git configuration:
   ```bash
   git config core.hooksPath scripts/git-hooks
   ```

### Benefits

- Ensures the `README.md` file is always accurate and up-to-date.
- Reduces manual effort and the risk of forgetting to update the device table.

### Adding the Hook to the Repository

To include the `pre-push` hook in the repository:
1. Place the hook script in the `scripts/git-hooks/` directory.
2. Ensure the hook is executable:
   ```bash
   chmod +x scripts/git-hooks/pre-push
   ```
3. Commit the hook to the repository:
   ```bash
   git add scripts/git-hooks/pre-push
   git commit -m "Add pre-push hook to update README.md"
   ```

### Notes

- The `pre-push` hook will only run locally on your machine. Collaborators must also configure their Git to use the custom hooks directory by running the `git config core.hooksPath` command.
- Ensure Python is installed and accessible on your system, as the hook relies on the `update_device_table.py` script.


