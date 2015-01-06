ssh $DEPLOY_USER@$DEPLOY_HOST "cd $DEPLOY_PATH && env/bin/pip install -r requirements.txt"
ssh $DEPLOY_USER@$DEPLOY_HOST "cd $DEPLOY_PATH && git pull origin master && /usr/bin/sv restart $DEPLOY_SERVICE"

