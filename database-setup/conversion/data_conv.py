import psycopg2
import psycopg2.extras
import sys
import os

db_name = 'trill'
db_user = 'trill'

def create_user(user_data):
    print("create_user()")
    query_stmt = 'SELECT id FROM users WHERE email = %s'
    insert_stmt = 'INSERT INTO users (firstname,surname,email,managerfirstname,managersurname,pwhash) VALUES (%s,%s,%s,%s,%s,%s) RETURNING id'
    c2.execute(query_stmt, (user_data['email'],))
    id = c2.fetchone()
    if id != None:
        print("create_user() - user already exists.. skipping")
        return id[0]
    c2.execute(insert_stmt, (user_data['firstname'],user_data['surname'],user_data['email'],user_data['managerfirstname'],user_data['managersurname'],user_data['encrypted_passwd']))
    id = c2.fetchone()
    print("create_user() - created new user")
    return id[0]

def create_trill_role_group(groupname):
    print("create_trill_role_group() - " + groupname)
    query_stmt = 'SELECT id FROM trill_role_groups WHERE groupname = %s'
    insert_stmt = 'INSERT INTO trill_role_groups (groupname) VALUES (%s) RETURNING id'
    c2.execute(query_stmt,(groupname,))
    id = c2.fetchone()
    if id != None:
        print("create_trill_role_group() - role group already exists.. skipping")
        return id[0]
    c2.execute(insert_stmt,(groupname,))
    id = c2.fetchone()
    print("create_trill_role_group() - created new role group " + groupname)
    return id[0]

def create_job_title(job_title, trill_role_group_id):
    print("create_job_title() - " + job_title)
    query_stmt = 'SELECT id FROM job_titles WHERE title = %s'
    insert_stmt = 'INSERT INTO job_titles (title,trill_role_group_id) VALUES (%s,%s) RETURNING id'
    c2.execute(query_stmt,(job_title,))
    id = c2.fetchone()
    if id != None:
        print("create_job_title() - job title already exists.. skipping")
        return id[0]
    c2.execute(insert_stmt,(job_title,trill_role_group_id))
    id = c2.fetchone()
    print("create_job_title() - created new job title " + job_title)
    return id[0]

def create_user_job(user_id, job_title_id):
    print("create_user_job()")
    query_stmt = 'SELECT id FROM user_jobs WHERE user_id = %s AND job_title_id = %s'
    insert_stmt = 'INSERT INTO user_jobs (user_id,job_title_id) VALUES (%s,%s) RETURNING id'
    c2.execute(query_stmt,(user_id,job_title_id))
    id = c2.fetchone()
    if id != None:
        print("create_user_job() - user/job title mapping already exists.. skipping")
        return id[0]
    c2.execute(insert_stmt,(user_id,job_title_id))
    id = c2.fetchone()
    print("create_user_job() - created new user/job title mapping")
    return id[0]

def create_skill_group(skillgroupname,skilltype):
    print("create_skill_group() - " + skillgroupname)
    query_stmt = 'SELECT id FROM skill_groups WHERE skillgroupname = %s'
    insert_stmt = 'INSERT INTO skill_groups (skillgroupname,skilltype) VALUES (%s,%s) RETURNING id'
    c2.execute(query_stmt,(skillgroupname,))
    id = c2.fetchone()
    if id != None:
        print("create_skill_group() - skill group already exists.. skipping")
        return id[0]
    c2.execute(insert_stmt,(skillgroupname,skilltype))
    id = c2.fetchone()
    print("create_skill_group() - created new role group " + skillgroupname)
    return id[0]

def create_skill_title(skilltitlename,skill_group_id):
    print("create_skill_title() - " + skilltitlename)
    query_stmt = 'SELECT id FROM skill_titles WHERE skilltitlename = %s'
    insert_stmt = 'INSERT INTO skill_titles (skilltitlename,skill_group_id) VALUES (%s,%s) RETURNING id'
    c2.execute(query_stmt,(skilltitlename,))
    id = c2.fetchone()
    if id != None:
        print("create_skill_title() - skill title already exists.. skipping")
        return id[0]
    c2.execute(insert_stmt,(skilltitlename,skill_group_id))
    id = c2.fetchone()
    print("create_skill_title() - created new skill title " + skilltitlename)
    return id[0]

def create_skill(skillcode,skilldescription,skill_title_id):
    print("create_skill() - " + skillcode)
    query_stmt = 'SELECT id FROM skills WHERE skillcode = %s'
    insert_stmt = 'INSERT INTO skills (skillcode,skilldescription,skill_title_id) VALUES (%s,%s,%s) RETURNING id'
    c2.execute(query_stmt,(skillcode,))
    id = c2.fetchone()
    if id != None:
        print("create_skill_title() - skill code already exists.. skipping")
        return id[0]
    c2.execute(insert_stmt,(skillcode,skilldescription,skill_title_id))
    id = c2.fetchone()
    print("create_skill_title() - created new skill - code " + skillcode)
    return id[0]

def get_role_group_id(groupname):
    query_stmt = 'SELECT id FROM trill_role_groups WHERE groupname = %s'
    c2.execute(query_stmt,(groupname,))
    id = c2.fetchone()
    if id != None:
        return id[0]
    else:
        print("Unable to create link - Role Group " + groupname + " not found in the database.")
        return 0

def get_skill_group_id(skillgroupname):
    query_stmt = 'SELECT id FROM skill_groups WHERE skillgroupname = %s'
    c2.execute(query_stmt,(skillgroupname,))
    id = c2.fetchone()
    if id != None:
        return id[0]
    else:
        print("Unable to create link - Skill Group " + skillgroupname + " not found in the database.")
        return 0

def create_role_group_link(skill_group,role_group):
    print("create_role_group_link - " + skill_group + " => " + role_group)
    query_stmt = 'SELECT id FROM trill_role_skill_groups WHERE trill_role_group_id = %s AND skill_group_id = %s'
    insert_stmt = 'INSERT INTO trill_role_skill_groups (trill_role_group_id,skill_group_id) VALUES (%s,%s) RETURNING id'
    trill_role_group_id = get_role_group_id(role_group)
    skill_group_id = get_skill_group_id(skill_group)
    if (trill_role_group_id == 0) or (skill_group_id == 0):
        return 0
    else:
        c2.execute(query_stmt,(trill_role_group_id, skill_group_id))
        id = c2.fetchone()
        if id != None:
            print("create_role_group_link - link already exists.. skipping")
            return 0
        c2.execute(insert_stmt,(trill_role_group_id, skill_group_id))
        id = c2.fetchone()
        print("create_role_group_link() - link created")
        return id[0]

def process_people_role():
    print("*************************************************")
    print("Processing People/Role data from staging table...")
    print("*************************************************")
    c1.execute("SELECT firstname,surname,email,managerfirstname,managersurname,encrypted_passwd,trill_role_group,job_title FROM people_role_stage")
    for r1 in c1:
        print("-------------------------------------------------------------------")
        print("Processing employee name " + r1['firstname'] + " " + r1['surname'])
        user_id = create_user(r1)
        trill_role_group_id = create_trill_role_group(r1['trill_role_group'],)
        job_title_id = create_job_title(r1['job_title'],trill_role_group_id)
        user_job_id = create_user_job(user_id,job_title_id)
        print("Completed processing employee name " + r1['firstname'] + " " + r1['surname'])
        print("Committing data for this employee to the database")
        dbconn.commit()
        print("-------------------------------------------------------------------")
    print("Finished processing People/Role data from staging table.")

def process_skill_groups():
    print("*************************************************")
    print("Processing Skill Group data from staging table...")
    print("*************************************************")
    c1.execute("SELECT skilltype,skillgroup,skilltitlename,skilldescription,skillcode FROM skill_mapping_stage")
    for r1 in c1:
        print("-------------------------------------------------------------------")
        print("Processing skill group " + r1['skillgroup'])
        skill_group_id = create_skill_group(r1['skillgroup'],r1['skilltype'])
        skill_title_id = create_skill_title(r1['skilltitlename'],skill_group_id)
        skill_id = create_skill(r1['skillcode'],r1['skilldescription'],skill_title_id)
        print("Completed processing skill group " + r1['skillgroup'])
        print("Committing data for this skill group to the database.")
        dbconn.commit()

        print("-------------------------------------------------------------------")
    print("Finished processing Skill Group data from staging table.")

def process_skill_role_links():
    print("******************************")
    print("Linking Roles and Skill Groups")
    print("******************************")
    c1.execute("SELECT skillgroup,trill_role_group FROM skill_role_stage")
    for r1 in c1:
        print("-------------------------------------------------------------------")
        print("Linking Skill Group <" + r1['skillgroup'] + "> => Role Group <" + r1['trill_role_group'] + " >")
        user_skill_id = create_role_group_link(r1['skillgroup'],r1['trill_role_group'])
        if user_skill_id > 0:
            print("Committing skill group/role link to the database")
            dbconn.commit()
        print("-------------------------------------------------------------------")
    print("Finished linking Roles and Skill Groups.")

def process_user_skills():
    print("***************************************************")
    print("Adding default proficiency, confidence and age data")
    print("***************************************************")
    c1.execute("DELETE FROM user_skills")
    c1.execute("INSERT INTO user_skills(user_id,skill_id,proficiency,confidence,age) SELECT u.id, s.id,1,1,1 FROM users u, skills s")
    print("Finished setting defaults.")
    dbconn.commit()


# DB connection for this run? And a cursor to run commands?
dbconn = psycopg2.connect(dbname=db_name, user=db_user)
c1 = dbconn.cursor(cursor_factory=psycopg2.extras.DictCursor)
c2 = dbconn.cursor(cursor_factory=psycopg2.extras.DictCursor)

process_people_role()
process_skill_groups()
process_skill_role_links()
process_user_skills()

c1.close()
c2.close()
dbconn.close()
