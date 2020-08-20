from xml.dom import minidom
import xml
import xmlformatter
import random


# This helps in creating root node for a xml file if for some reason the xml file contain unintended characters.
def create_root(file: str, root: str):
	xml_str = f"<{root}></{root}>"
	f = open(file, 'w+')
	f.write(xml_str)
	f.close()


def create_id():
	l = []
	for a in range(4):
		l.append(str(random.randint(1000, 9999)))
	return '-'.join(l)


def execute(func: list):
	"""
	:param func: This is a list containing [function, file, Name]
	:return: depends upon the function.
	"""
	func_len = len(func)
	if func_len > 0 and func[0] in commands:
		if (func[0] in ["create", "remove"] and func_len < 3) or (func[0] in ["save", "preview"] and func_len < 2):
			print("More information required to execute the given command")
			print("Type help for more information")
		elif func[0] == "create":
			file = file_dict[func[1]]
			file.create(func[2])
		elif func[0] == "remove":
			file = file_dict[func[1]]
			file.remove(func[2])
		elif func[0] == "save":
			file = file_dict[func[1]]
			file.save()
		elif func[0] == "preview":
			print(file_dict[func[1]])
		elif func[0] == "help":
			help()
	else:
		print("Invalid command")


def help():
	print("""
	NOTE: The commands are not case sensitive
	NOTE: For commands save, help and exit the trailing data will be ignored.
	NOTE: ANd for create and remove commands the trailing data will be considered as a part of name.
	Commands:
	create <client|product> <Name>
	remove <client|product> <Name>
	save
	preview <client|product>
	help
	exit
	""")


class Client:
	root = 'client'

	def __init__(self, file):
		self.file = file  # File name of the client xml.
		try:
			self.document = minidom.parse(file)  # minidom document object of client xml file.
		except xml.parsers.expat.ExpatError:  # Exception handling in case the file is empty
			create_root(file, self.root)
			self.document = minidom.parse(file)

	def create(self, client_name):
		id_val = create_id()
		# Create <data /> node
		data_node = self.document.createElement("data")

		# Create <id />
		id_node = self.document.createElement("id")
		id_text = self.document.createTextNode(str(id_val))
		id_node.appendChild(id_text)  # Create <id>id_text</id>

		# Create <name /> node
		name_node = self.document.createElement('name')
		name_txt = self.document.createTextNode(client_name)

		# Create <name>name_txt</name> node
		name_node.appendChild(name_txt)

		data_node.appendChild(id_node)
		data_node.appendChild(name_node)
		self.document.childNodes[-1].appendChild(data_node)

	def remove(self, client_name):
		for data in self.document.getElementsByTagName('name'):
			if data.firstChild.nodeValue == client_name:
				parent = data.parentNode
				parent.parentNode.removeChild(parent)

	def save(self):  # This will write the changes to the file thereby making the changes permanent.
		xml_str = formatter.format_string(self.document.toxml(encoding="UTF-8")).decode()
		f = open(self.file, 'w+')
		f.write(xml_str)
		f.close()

	def __str__(self):  # This will print the current status of the file in console.
		xml_str = formatter.format_string(self.document.toxml(encoding="UTF-8")).decode()
		return xml_str


class Product(Client):
	root = 'product'


prod_obj = Product('util\\product.xml')
cli_obj = Client('util\\client.xml')
formatter = xmlformatter.Formatter()
commands = ["help", "create", "remove", "save", "preview", "exit"]
file_dict = {"client": cli_obj, "product": prod_obj}

if __name__ == '__main__':
	print("=====YOU ARE RUNNING THIS FILE DIRECTLY=====")
	prod_obj = Product('product.xml')
	cli_obj = Client('client.xml')
	# Test Cases just remove the comments.
	# cli_obj.create('test')
	# cli_obj.remove('test')
	# prod_obj.create('test')
	# prod_obj.remove('test')
	# print(cli_obj)
	# print(prod_obj)
	# cli_obj.save()
	# prod_obj.save()
