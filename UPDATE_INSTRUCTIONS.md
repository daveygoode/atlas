# Updating ATLAS Framework

The ATLAS framework can be updated to get the latest instructions, improvements, and features.

## Quick Update

From your project root (not inside .atlas), run:

```bash
python .atlas/scripts/update_atlas.py
```

Or use the shell wrapper:

```bash
.atlas/scripts/update.sh
```

## What the Update Does

1. **Checks Git Status** - Ensures no uncommitted changes in .atlas/
2. **Backs Up Customizations** - Saves your project-specific files:
   - SHORT_IMPORTANT_MEMORY.md
   - CLAUDE_PROJECT_SPECIFIC.md
   - Session data
3. **Pulls Latest Changes** - Gets newest instructions and scripts from ATLAS repo
4. **Updates Project Files** - Updates your project's CLAUDE.md with new structure
5. **Restores Customizations** - Puts back your project-specific content
6. **Shows Changelog** - Displays recent updates

## Important Notes

- Backups are saved to `.atlas/backups/[timestamp]/`
- Your session data and project-specific content are preserved
- The updater won't proceed if you have uncommitted changes in .atlas/

## Manual Update (Alternative)

If you prefer to update manually:

```bash
cd .atlas
git fetch origin main
git pull origin main
cd ..
python .atlas/scripts/migrate_existing_project.py
```

## Troubleshooting

If the update fails:
1. Check the error message
2. Your backups are in `.atlas/backups/[timestamp]/`
3. You can manually restore from backups if needed
4. Submit issues at: https://github.com/daveygoode/atlas/issues

## Keeping Current

Run the update script periodically to get:
- Latest best practices and conventions
- New features and capabilities
- Security updates and improvements
- Enhanced documentation

Remember: ATLAS evolves with every project, and updates ensure you benefit from collective improvements!