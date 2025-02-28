// --------------------------------------------------------------------- //
// ##################################################################### //
//                            Classe Observador                          //
// ##################################################################### //
// --------------------------------------------------------------------- //

// Ideia desse Padrão de Projeto:
// Toda vez que um evento acontece, os observadores desse evento serão notificados e executados.

class Observador{

  constructor(){
    this.inscritos = [];
  }

  adiciona(funcao){
    this.inscritos.push(funcao)
  }

  remove(){
    this.inscritos = this.inscritos.filter((f)=> f !== funcao);
  }

  notifica(id,historicoTimes,nomesCompleto){

    for (let i = 0;i<this.inscritos.length;i++){
      this.inscritos[i](id,historicoTimes,nomesCompleto );
    }

  }

}


// --------------------------------------------------------------------- //
// ##################################################################### //
//                             Classe Tabela                             //
// ##################################################################### //
// --------------------------------------------------------------------- //

class Dados {

    time1 = ""; time2 = "";
    gol_time1 = ""; gol_time2 = "";
    dados_time1 = [0, 0, 0, 0, 0, 0, 0, 0]; dados_time2 = [0, 0, 0, 0, 0, 0, 0, 0];
    array = ["FLA", "PAL", "FLU", "SAO", "SAN", "CAM","CFC", "COR", "CAP", "FOR", "BOT", "JUV",
      "CUI", "GOI", "BRA", "ACG", "INT", "CEA", "AVA", "AMG"];
    nome_original = ["Flamengo","Palmeiras","Fluminense","São Paulo","Santos","Atlético-MG","Coritiba","Corinthians","Athlético-PR","Fortaleza",
      "Botafogo","Juventude","Cuiabá","Goiás","Bragantino","Atlético-GO","Internacional","Ceará","Avaí","América-MG"];
    dados = new Map();
    historico_Obj = new Historico();
  
    constructor() {
  
      for (let x of this.array) {
        this.dados.set(x, [0, 0, 0, 0, 0, 0, 0, 0])
      };
      
    };
  
    computaDados() {
  
      //FORMATACAO DO HASHMAP "nome": [pontos, partidas, vitorias, empates, derrotas, saldo_de_gols, gols_pro, gols_contra]
  
      let dados = this.dados; let time1 = this.time1; let time2 = this.time2; let gol_time1 = this.gol_time1; let gol_time2 = this.gol_time2;
      let dados_time1 = this.dados_time1; let dados_time2 = this.dados_time2;
  
      for (let i = 0; i < 33; i++) {
        for (let j = 0; j < 10; j++) {
  
          time1 = rodadas[i][j].substring(0, 3);
          time2 = rodadas[i][j].substring(6, 9);
          gol_time1 = parseInt(rodadas[i][j].substring(4, 5));
          gol_time2 = parseInt(rodadas[i][j].substring(10, 11));
  
          dados_time1 = dados.get(time1);
          dados_time2 = dados.get(time2);
  
          if (gol_time1 > gol_time2) {

            dados_time1[0] += 3;//contabiliza pontos
            dados_time1[1] += 1;//contabiliza partidas
            dados_time1[2] += 1;//contabiliza vitoria
            //dados_time1[3] = dados_time1[1];
            //dados_time1[4] = dados_time1[2];
            dados_time1[5] += (gol_time1 - gol_time2);//saldo de gols
            dados_time1[6] += gol_time1;//gols pro
            dados_time1[7] += gol_time2;//gols contra
            dados.set(time1, dados_time1);
  
            //TIME 2 PERDEU
            dados_time2[0] += 0;//contabiliza pontos
            dados_time2[1] += 1;//contabiliza partidas
            //dados_time2[2] = dados_time2[0];
            //dados_time2[3] = dados_time2[1];
            dados_time2[4] += 1;//contabiliza derrota
            dados_time2[5] += (gol_time2 - gol_time1);//saldo de gols
            dados_time2[6] += gol_time2;//gols pro
            dados_time2[7] += gol_time1;//gols contra
            dados.set(time2, dados_time2);

        } else {

            if (gol_time1 < gol_time2) {

              dados_time2[0] += 3;//contabiliza pontos
              dados_time2[1] += 1;//contabiliza partidas
              dados_time2[2] += 1;//contabiliza vitoria
              //dados_time2[3] = dados_time2[1];
              //dados_time2[4] = dados_time2[2];
              dados_time2[5] += (gol_time2 - gol_time1);//saldo de gols
              dados_time2[6] += gol_time2;//gols pro
              dados_time2[7] += gol_time1;//gols contra
              dados.set(time2, dados_time2);
  
              //TIME 1 PERDEU
              dados_time1[0] += 0;//contabiliza pontos
              dados_time1[1] += 1;//contabiliza partidas
              //dados_time1[2] = dados_time1[0];
              //dados_time1[3] = dados_time1[1];
              dados_time1[4] += 1;//contabiliza derrota
              dados_time1[5] += (gol_time1 - gol_time2);//saldo de gols
              dados_time1[6] += gol_time1;//gols pro
              dados_time1[7] += gol_time2;//gols contra
              dados.set(time1, dados_time1);

            }
            else {

              dados_time2[0] += 1;//contabiliza pontos
              dados_time2[1] += 1;//contabiliza partidas
              //dados_time2[2] += 0;
              dados_time2[3] += 1;//contabiliza empate
              //dados_time2[4] += 0;
              dados_time2[5] += (gol_time2 - gol_time1);//saldo de gols
              dados_time2[6] += gol_time2;//gols pro
              dados_time2[7] += gol_time1;//gols contra
              dados.set(time2, dados_time2);
  
              //TIME 2 EMPATOU
              dados_time1[0] += 1;//contabiliza pontos
              dados_time1[1] += 1;//contabiliza partidas
              //dados_time1[2] += 1;
              dados_time1[3] += 1;//contabiliza empate
              //dados_time1[4] += 0;
              dados_time1[5] += (gol_time1 - gol_time2);//saldo de gols
              dados_time1[6] += gol_time1;//gols pro
              dados_time1[7] += gol_time2;//gols contra
              dados.set(time1, dados_time1);

            };
          };
        };
        this.historico_Obj.calculaHistorico(dados, i); 
      };
      // return dados;
    };
  
    getHistorico(){
      return (this.historico_Obj.dados_historico);
    }

    getDados(){
      return this.dados;
    }

    getChavesOrdenado(){
      let mapa_ordenado = new OrdenaMapa();
      let chaves = mapa_ordenado.inOrder(mapa_retorno);
      return chaves;
    }
  
    escrevaDados(chaves,mapa_retorno){
      let ids = ["primeiro","segundo","terceiro","quarto","quinto","sexto",
                  "setimo","oitavo","nono","decimo","decimoPrimeiro","decimoSegundo",
                  "decimoTerceiro","decimoQuarto","decimoQuinto","decimoSexto","decimoSetimo",
                  "decimoOitavo","decimoNono","vigesimo"];
      let timeIndice = 0;
      let dadosTime;
      
      
      for (let id of ids){
        document.getElementById(id).innerHTML = chaves[timeIndice];
        dadosTime = mapa_retorno.get(chaves[timeIndice]);
        document.getElementById(id+"PTS").innerHTML = dadosTime[0];
        document.getElementById(id+"Partidas").innerHTML = dadosTime[1];
        document.getElementById(id+"Vitorias").innerHTML = dadosTime[2];
        document.getElementById(id+"Empates").innerHTML = dadosTime[3];
        document.getElementById(id+"Derrotas").innerHTML = dadosTime[4];
        document.getElementById(id+"Saldo").innerHTML = dadosTime[5];
        document.getElementById(id+"ProGols").innerHTML = dadosTime[6];
        document.getElementById(id+"ContraGols").innerHTML = dadosTime[7];
        timeIndice += 1;
      };
    };
  
    toNomeCompleto(){
  
      let nomesCompleto = new Map();
      let cont2 = 0;
      for (let t of this.array){
        nomesCompleto.set(t,this.nome_original[cont2]);
        cont2+=1;
      }
  
      this.nome_original = [];
      return nomesCompleto;
    };
  };

// --------------------------------------------------------------------- //
// ##################################################################### //
//                         Classe Ordena Mapa                            //
// ##################################################################### //
// --------------------------------------------------------------------- //

class OrdenaMapa{

    array = [];
    
    constructor(){};
  
    inOrder(mapa){
  
      let array = new Array(20);
      let cont = 0;
  
      for (let x of mapa.keys()){
        array[cont] = x;
        cont += 1;
      }

      for (let i=1;i<20;i++){
        for (let j=0; j<i; j++){

            let pontos1 = mapa.get(array[i])[0];
            let pontos2 = mapa.get(array[j])[0];
            let saldo1 = mapa.get(array[i])[5];
            let saldo2 = mapa.get(array[j])[5];
            let gols_pro1 = mapa.get(array[i])[6];
            let gols_pro2 = mapa.get(array[j])[6];
            
            if (pontos1 > pontos2){//ordena por pontos
                let temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
            else if(saldo1 > saldo2 && pontos1 == pontos2){//ordena por saldo
                let temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
            else if (saldo1 == saldo2 && pontos1 == pontos2 && gols_pro1 > gols_pro2){//ordena por vitoria
                let temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            };
        };
      };
      return array;
    };
};

// --------------------------------------------------------------------- //
// ##################################################################### //
//                          Classe Historico                             //
// ##################################################################### //
// --------------------------------------------------------------------- //

class Historico{

    dados_historico = new Map();
    mapa_ordenado = new OrdenaMapa();
    array = ["FLA", "PAL", "FLU", "SAO", "SAN", "CAM", "CAP", "CFC", "COR", "CAP", "FOR", "BOT", "JUV",
    "CUI", "GOI", "BRA", "ACG", "INT", "CEA", "AVA", "AMG"];
  
    constructor(){

      for(let x of this.array){
          this.dados_historico.set(x, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]);
      }

    }
  
    calculaHistorico(dados,rodada){
  
      let chaves = this.mapa_ordenado.inOrder(dados)
      for (let p of chaves){
        let copia = this.dados_historico.get(p);
        copia[rodada] = chaves.indexOf(p) + 1;
        this.dados_historico.set(p, copia);
      };
    };
  
    getHistorico(key){
      return this.dados_historico.get(key);
    };
};


// --------------------------------------------------------------------- //
// ##################################################################### //
//                               MAIN                                    //
// ##################################################################### //
// --------------------------------------------------------------------- //

let rodadas = JSON.parse(localStorage.getItem('rodadas'))
let mapa_dados = new Dados();
mapa_dados.computaDados();
let mapa_retorno = mapa_dados.getDados();
let chaves = mapa_dados.getChavesOrdenado();
mapa_dados.escrevaDados(chaves,mapa_retorno);
let historicoTimes = mapa_dados.getHistorico();
let nomesCompleto = mapa_dados.toNomeCompleto();
let myChart = null;
let observador = new Observador();
observador.adiciona(criaGrafico);
let posAnt;


function detalhesClicado(id,historicoTimes,nomesCompleto){
  observador.notifica(id,historicoTimes,nomesCompleto);
}

// Equivalente às classes e métodos que criam o gráfico no código em JAVA.
function criaGrafico(id,historicoTimes,nomesCompleto) {

  let img;
  let pos = ((id.id)[0]).toUpperCase() + (id.id).slice(1);

  if (myChart != null){
    // Limpa o grafico e arruma os valores do botoes.
    myChart.destroy();
    myChart = null;

    document.getElementById("button"+pos).value = "Detalhes";
    if (document.getElementById("button"+posAnt).value == "Voltar"){
      document.getElementById("button"+posAnt).value = "Detalhes";
    };
    
    img = document.getElementById("escudo");
    document.getElementById("ClubeEscudo").removeChild(img);  
    document.getElementById("clube").innerHTML = "Clique em Detalhes!";

  }
  else{

    // Desenha o grafico
    document.getElementById("clube").innerHTML = "";
    let time = id.innerText;
    posAnt = pos;
    img = document.createElement("img");
    img.src = "Escudos/"+time+".png";
    img.style.width = "48px"; 
    img.style.height = "48px";
    img.id = "escudo";
    document.getElementById("clube").innerHTML = nomesCompleto.get(time);
    document.getElementById('ClubeEscudo').appendChild(img);
    
    
    let posicoes = historicoTimes.get(time);
    let rodadas = ['1', '2', '3', '4', '5',
      '6', '7', '8', '8', '9', '10', '11', '12', '13', '14', '15', '16',
      '17', '18', '19', '20', '21','22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33'];

    const data = {

      labels: rodadas,
      datasets: [{
        label: time,
        backgroundColor: 'rgb(0, 173, 181)',
        borderColor: 'rgb(0, 173, 181)',
        pointBackgroundColor:'rgb(57, 62, 70)',
        pointBorderColor:'rgb(0, 173, 181)',  
        data: posicoes,
        pointRadius:5,
        borderColor:"rgba(0,173,181,1.000)"
      }]
    };
    const config = {
      type: 'line',
      data: data,
      options: {
        responsive:true,
        scales: {
          y: {
            reverse: true,
            max: 20,
            min: 0,
            ticks: {color:"gray"},
            grid:{borderColor:'gray',color:"gray"}
          },
          x:{
            title:{display:true,text:"Rodadas X Posição",font:{weight:"bold",size:18},color:"white"},
            grid:{borderColor:'gray',color:"gray"},
            ticks: {color:"gray"}
          }
        }
      }
    };
    myChart = new Chart(document.getElementById('canva'),config);
    document.getElementById("button"+pos).value = "Voltar";
  };
};
