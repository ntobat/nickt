from flask.ext.login import UserMixin

class UserNotFoundError(Exception):
	pass
	
class User(UserMixin):
	USER = {'nick': 'password'}

	def __init__(self, id):
		if not id in self.USER:
			raise UserNotFoundError()
		self.id = id
		self.password = self.USER[id]

	@classmethod
	def get(self_class, id):
		try:
			return self_class(id)
		except UserNotFoundError:
			return None

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		try:
			return unicode(self.id)  # python 2
		except NameError:
			return str(self.id)  # python 3

	def __repr__(self):
		return '<User %r' % (self.nickname)