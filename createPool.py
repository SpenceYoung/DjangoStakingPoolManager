#Use the below command after you input your desired pool name for the "poolName" string
#python manage.py shell < createPool.py
from users.models import PoolManager

def createNewPool():
	poolName = "algo"#str(input("Enter the name (crypto ticker) of your new pool"))
	poolName = poolName.upper()
	pool = PoolManager(cryptoName = poolName, total= 0.0)
	pool.save()

def addAddress(poolName, addy):
	pool = PoolManager.objects.get(name=poolName.upper())[0]
	pool.cryptoAddress = addy
	pool.save()
#createNewPool()

