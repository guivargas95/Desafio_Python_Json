# Desafio_Python_Json

<p>O objetivo do desafio é construir um Parser para o arquivo de log Quake.txt</p>
<p>O arquivo "Quake.txt" é gerado pelo servidor de Quake 3 Arena. Nele está registrado informações sobre as partidas, informações como: Quando começa, quando termina, quem matou quem, quem "se matou" (caiu no vazio, explodiu a si próprio), entre outros. O Parser deve ser capaz de ler o arquivo, agrupar os dados de cada partida, e organizar as suas informações.</p>
<p>Para cada jogo o Parser deve gerar algo como:</p>


~~~[{
  "game": 1,
  "status": {
     "total_kills": 45,
     "players": [
		{
			"id": 1,
			"nome": "Mocinha",
			"kills": 5,
			"old_names": ["Dono da bola"]
		},
		{
			"id": 2,
			"nome": "Isgalamido",
			"kills": 18,
			"old_names": []
		},
		{
			"id": 3,
			"nome": "Zeh",
			"kills": 20,
			"old_names": []
		}
	]
  }
}]
~~~
<h2>Observações:</h2>
<p>Quando o <world> mata o player ele perde -1 kill. <world> não é um player e não deve aparecer na lista de players e nem no dicionário de kills. total_kills são os kills dos games, isso inclui mortes do <world>.O Comando ClientUserinfoChanged indica a definição do nome do jogador.

