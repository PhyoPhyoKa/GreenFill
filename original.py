# @app.route('/updateUser/<int:id>/', methods=['GET','POST'])
# @login_required
# def update_user(id):
#     update_user_form = CreateUserForm(request.form)
#     update_password_form = UpdatePasswordForm(request.form)
#
#     # if request.method == 'POST' and update_user_form.validate():
#     #     print("POST request received. Form validated.")  # Debug print
#     if request.method == 'POST':
#         if update_user_form.submit.data and update_user_form.validate():
#
#             print("POST request received. Form validated.")  # Debug print
#             users_dict = {}
#             db = shelve.open('user.db', 'w')
#             users_dict = db['Users']
#
#             user = users_dict.get(id)
#             if user:
#                 user.set_username(update_user_form.username.data)
#                 user.set_email(update_user_form.email.data)
#                 # user.set_password(update_user_form.password.data)
#
#                 db['Users'] = users_dict
#                 db.close()
#
#                 print("User details updated. Redirecting...")  # Debug print
#             # if current_user.get_user_id() == 1:  # Admin
#             #     return redirect(url_for('retrieve_users', id=1))
#             # #     # return redirect('/')
#             # else:
#                 return redirect(url_for('retrieve_users', id=current_user.get_user_id()))
#                 # return redirect('/')
#             else:
#                 print("User not found.")  # Debug if user is missing
#                 flash("User not found.")
#                 return redirect(url_for('home'))
#
        # elif update_password_form.submit.data and update_password_form.validate():
        #     db = shelve.open('user.db', 'w')
        #     users_dict = db['Users']
        #     user = users_dict.get(id)
        #
        #     if user:
        #         if not check_password_hash(user['password'], update_password_form.current_password.data):
        #             flash("Current password is incorrect.")
        #         else:
        #             user['password'] = generate_password_hash(update_password_form.new_password.data)
        #             db['Users'] = users_dict
        #             db.close()
        #
        #             flash("Password updated successfully.")
        #             return redirect(url_for('retrieve_users', id=current_user.get_user_id()))
            db.close()
#         print("Form validation failed.")
#         print(update_user_form.errors)
#         print(update_password_form.errors)
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
#         return render_template('updateUser.html', form=update_user_form, password_form=update_password_form)
#
#
# <br><br>
#     <form method="POST" action="">
#         <h3>Change Password</h3>
#         <div class="form-group">
#             {{ render_field(password_form.current_password, class="form-control") }}
#         </div>
#
#         <div class="form-group">
#             {{ render_field(password_form.new_password, class="form-control") }}
#         </div>
#
#         <div class="form-group">
#             {{ render_field(password_form.confirm_password, class="form-control") }}
#         </div>
#
#         <br>
#         <input type="submit" value="Change Password" class="btn btn-warning" />