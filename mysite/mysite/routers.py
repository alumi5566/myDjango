class CloudDBRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == "oracleDB":
            return "second_db"
        elif model._meta.app_label == "awsRDS":
            return 'aws_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == "oracleDB":
            return "second_db"
        elif model._meta.app_label == "awsRDS":
            return 'aws_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == "oracleDB" or obj2._meta.app_label == "oracleDB":
            return True
        elif obj1._meta.app_label == "awsRDS" or obj2._meta.app_label == "awsRDS":
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == "oracleDB":
            return False
        elif app_label == "awsRDS":
            return db == 'aws_db'
        return False