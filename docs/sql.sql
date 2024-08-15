python manage.py sqlmigrate reader 0001 --settings=config.settings.dev
BEGIN;
--
-- Create model Reader
--
CREATE TABLE "reader_reader" ("password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "first_name" varchar(150) NOT NULL, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "username" varchar(50) NOT NULL PRIMARY KEY, "title" varchar(5) NULL);
CREATE TABLE "reader_reader_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "reader_id" varchar(50) NOT NULL REFERENCES "reader_reader" ("username") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "reader_reader_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "reader_id" varchar(50) NOT NULL REFERENCES "reader_reader" ("username") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create constraint reader_reader_title_check on model reader
--
CREATE TABLE "new__reader_reader" ("password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "first_name" varchar(150) NOT NULL, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "username" varchar(50) NOT NULL PRIMARY KEY, "title" varchar(5) NULL, CONSTRAINT "reader_reader_title_check" CHECK ("title" IN ('Mr', 'Mrs', 'Dr')));
INSERT INTO "new__reader_reader" ("password", "last_login", "is_superuser", "first_name", "last_name", "email", "is_staff", "is_active", "date_joined", "username", "title") SELECT "password", "last_login", "is_superuser", "first_name", "last_name", "email", "is_staff", "is_active", "date_joined", "username", "title" FROM "reader_reader";
DROP TABLE "reader_reader";
ALTER TABLE "new__reader_reader" RENAME TO "reader_reader";
CREATE UNIQUE INDEX "reader_reader_groups_reader_id_group_id_177e914e_uniq" ON "reader_reader_groups" ("reader_id", "group_id");
CREATE INDEX "reader_reader_groups_reader_id_45bdeb9d" ON "reader_reader_groups" ("reader_id");
CREATE INDEX "reader_reader_groups_group_id_934eaea6" ON "reader_reader_groups" ("group_id");
CREATE UNIQUE INDEX "reader_reader_user_permissions_reader_id_permission_id_8ce24cc6_uniq" ON "reader_reader_user_permissions" ("reader_id", "permission_id");
CREATE INDEX "reader_reader_user_permissions_reader_id_09b2ee0a" ON "reader_reader_user_permissions" ("reader_id");
CREATE INDEX "reader_reader_user_permissions_permission_id_1f896ac4" ON "reader_reader_user_permissions" ("permission_id");
COMMIT;
