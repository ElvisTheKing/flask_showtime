ssh $DEPLOY_USER@$DEPLOY_HOST "cd $DEPLOY_PATH && git pull origin master"
ssh $DEPLOY_USER@$DEPLOY_HOST "cd $DEPLOY_PATH && env/bin/pip install -r requirements.txt"
ssh $DEPLOY_USER@$DEPLOY_HOST "cd $DEPLOY_PATH && env/bin/python ./manager.py db upgrade"
ssh $DEPLOY_USER@$DEPLOY_HOST  "/usr/bin/sv restart $DEPLOY_SERVICE"

