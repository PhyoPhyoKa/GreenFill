# from flask import Flask, render_template, request, redirect, url_for, flash
# import shelve,User
# from User import User
# from Forms import CreateUserForm, LogInForm, UpdatePasswordForm
# from flask_login import LoginManager, login_user, login_required,logout_user,current_user
# from werkzeug.security import generate_password_hash, check_password_hash
#
# app = Flask(__name__)
# app.secret_key = 'secret key'
#
#
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'
#
#
# @login_manager.user_loader
# def load_user(user_id):
#     with shelve.open(User.user_db_file) as db:
#         users_dict = db.get('Users', {})
#         user_data = users_dict.get(int(user_id))
#         if user_data:
#             return user_data  # User already has the correct ID from the database
#     return None
#
#
# @app.route('/')
# def home():
#     return render_template('home.html', user=current_user)
#
#
# @app.route('/createUser', methods=['GET','POST'])
# def create_user():
#     create_user_form = CreateUserForm(request.form)
#     if request.method == 'POST' and create_user_form.validate():
#         users_dict = {}
#         db = shelve.open('user.db', 'c')
#
#         try:
#             users_dict = db['Users']
#         except:
#             print('Error in retrieving Users from user.db')
#
#         user = User(create_user_form.username.data, create_user_form.email.data, create_user_form.password.data)
#         users_dict[user.get_user_id()] = user
#         db['Users'] = users_dict
#         print(users_dict)
#
#         # Test codes
#         users_dict = db['Users']
#         user = users_dict[user.get_user_id()]
#         print(user.get_username(), 'was stored in user.db successfully with the user__id==', user.get_user_id())
#
#         db.close()
#
#         return redirect(url_for('login'))
#     return render_template('createUser.html', form=create_user_form)
#
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     login_form = LogInForm(request.form)
#
#     if request.method == 'POST' and login_form.validate():
#         email = login_form.email.data
#         password = login_form.password.data
#
#         with shelve.open(User.user_db_file) as db:
#             users_dict = db.get('Users', {})
#
#             user = None
#             for user_id, user_data in users_dict.items():
#                 if user_data.get_email() == email:
#                     if user_data.verify_password(password):
#                         user = user_data
#
#                         user.set_id(int(user_id))
#                         login_user(user)
#                         flash("successfully logged in!")
#                         return redirect(url_for('home'))
#                     else:
#                         flash("Invalid email or password.")
#                         break
#
#     return render_template('login.html', form=login_form)
#
#
# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     flash("You have been logged out.")
#     return redirect(url_for('home'))
#
#
# @app.route('/retrieveUsers/<int:id>/')
# @login_required
# def retrieve_users(id):
#     if current_user.get_user_id() != id and current_user.get_user_id() != 1:
#         flash("You are not authorized to view this page.")
#         return redirect(url_for('home'))
#
#     users_dict = {}
#     db = shelve.open('user.db', 'r')
#     users_dict = db['Users']
#     db.close()
#
#     users_list = []
#     if id == 1:
#         for key in users_dict:
#             user = users_dict.get(key)
#             users_list.append(user)
#
#     else:
#         user = users_dict.get(id)
#         if user:
#             users_list.append(user)
#
#     return render_template('retrieveUsers.html', count=len(users_list), users_list=users_list)
#
#
# @app.route('/updateUser/<int:id>/', methods=['GET','POST'])
# @login_required
# def update_user(id):
#     update_user_form = CreateUserForm(request.form)
#
#     # if request.method == 'POST' and update_user_form.validate():
#     #     print("POST request received. Form validated.")  # Debug print
#     if request.method == 'POST':
#         if not update_user_form.validate():
#             print("Form validation failed.")  # Debugging
#             print(update_user_form.errors)  # Show errors to help debug
#         else:
#             print("POST request received. Form validated.")  # Debug print
#         users_dict = {}
#         db = shelve.open('user.db', 'w')
#         users_dict = db['Users']
#
#         user = users_dict.get(id)
#         if user:
#             user.set_username(update_user_form.username.data)
#             user.set_email(update_user_form.email.data)
#             # user.set_password(update_user_form.password.data)
#
#             db['Users'] = users_dict
#             db.close()
#
#             print("User details updated. Redirecting...")  # Debug print
#             # if current_user.get_user_id() == 1:  # Admin
#             #     return redirect(url_for('retrieve_users', id=1))
#             # #     # return redirect('/')
#             # else:
#             return redirect(url_for('retrieve_users', id=current_user.get_user_id()))
#                 # return redirect('/')
#         else:
#             print("User not found.")  # Debug if user is missing
#             flash("User not found.")
#             return redirect(url_for('home'))
#
#
#     else:
#         print("GET request to update user form.")  # Debug print
#         users_dict = {}
#         db = shelve.open('user.db', 'r')
#         users_dict = db['Users']
#         db.close()
#
#         user = users_dict.get(id)
#         if user:
#             update_user_form.username.data = user.get_username()
#             update_user_form.email.data = user.get_email()
#             # update_user_form.password.data = user.get_password()
#
#         return render_template('updateUser.html', form=update_user_form)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
