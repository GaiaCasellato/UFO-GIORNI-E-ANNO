from database.DB_connect import DBConnect
from model.State import State


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllStates():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select * from state s  """
        cursor.execute(query)
        for row in cursor:
            result.append(State(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchi():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select n.state1 , n.state2 
                    from sighting s , neighbor n
                    where (s.state  = n.state1 or s.state  = n.state2) and n.state1 < n.state2 
                    group by n.state1 , n.state2  """
        cursor.execute(query, )
        for row in cursor:
            result.append((row['state1'], row['state2']))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPeso(anno, giorno, stato1, stato2 ):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ select count(distinct s1.state , s2.state) as peso
                    from sighting s1 , sighting s2
                    where year(s1.`datetime`) = year(s2.`datetime`) and year(s1.`datetime`) = %s
                    and datediff(s1.`datetime`, s2.`datetime`) <= %s
                    and s1.state < s2.state 
                    and s1.state = %s and s2.state = %s """
        cursor.execute(query,(anno, giorno, stato1, stato2,))
        for row in cursor:
            result.append(row["peso"])
        cursor.close()
        conn.close()
        return result


