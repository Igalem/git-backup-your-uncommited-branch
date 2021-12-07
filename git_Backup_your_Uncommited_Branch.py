#!/usr/bin/python
#
# ---- Backup your Uncommitted GIT Branch ----
# 
# Use this script to buckup you uncommited changes in your Git branch
#
# Version : 1.0v
# 
#

import sys
import os

## You can setup manualy your default paths: ########################################################

# --- Git Master/Head path:
# gitPathMaster = '$GIT_MASTER_USER_PATH'	

# --- Backup path:
# gitPathByUser = '$USER_PATH/BranchBackup/gitBackup'

# --- Log path:
# gitLogPath = '$USER_PATH/BranchBackup/log'

#####################################################################################


print('\033c')
print('        ***** Automation Backuping process for git Branch ***** \n')

gitPathMaster = str(input('Enter git master direcory: '))

gitBranchName = str(input('Enter your Branch name: '))

gitPathByUser = str(input('Enter backup direcory: '))

gitLogPath = str(input('Enter git Log direcory: '))

##----------------------------------------------------------------------------------------

gitPathBackup = gitPathByUser + '/' + gitBranchName
gitLog = gitLogPath +'/git_' + gitBranchName + '.log'

os.chdir(gitPathMaster)

### Invoke Branch Name
os.system('git branch --show-current > ' + gitLog)

### List git Status
os.system('git status --short >> ' + gitLog)

gitLogOpen = open(gitLog, 'r')
gitStatus = []
gitDirectories = []
gitFiles = []

for i, row in enumerate(gitLogOpen):
	gitStatus.append(row.strip())
	if i>0: ### Ignore first row & Append Only Directories&Filenames Path
		if row.split()[0].upper() != 'D' and row.count('/') > 0:
			gitDirectories.append(('/').join(row.split()[1].split('/')[:-1]))
			gitFiles.append(('/').join(row.split()[1].split('/')[-1:]))

##print(len(gitStatus))

if len(gitStatus) == 1:
	print('No Changes Found in branch name: ' + gitStatus[0])
	print('Process ended. \n')
	exit(0)
else:
	print('Backuping brnach: ' + gitStatus[0] + '\n')	
	

for dir, file in zip(gitDirectories, gitFiles):
	## print(dir + '	' + file)
	bckFullPath = gitPathBackup + '/' + dir 
	copyFile1 = gitPathMaster + '/' + dir + '/' + file
	copyFile2 = gitPathBackup + '/' + dir + '/' + file
	
	try: ### Trying to create backup folder structure
		print('Creating backup brnach direcory:')
		print(bckFullPath)
		os.makedirs(bckFullPath, exist_ok=True)
	except:
		exit(1)
	else:
		print('Direcoty created.')

	try:
		print('Copying file/s:')
		print(file)
		os.system('cp ' + copyFile1 + ' ' + copyFile2)	
	except:
		exit(1)
	else:
		print('Filename/s copied.')		


print('\n')
#os.system('git checkout --quiet master')
gitLogOpen.close()
##os.system('rm ' + gitLog)
