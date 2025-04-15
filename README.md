# Muh_zica - Linguagem de Programação Musical

### **Motivação**
Muh_zica é uma linguagem de programação projetada para criar música de forma simples e programática. Seu objetivo é permitir que qualquer pessoa, mesmo sem conhecimento musical profundo, componha melodias e explore o mundo da programação e da música de forma integrada. Com Muh_zica, programadores podem transformar código em música, abrindo portas para aprendizado musical e criação artística.

---

### **Características**
- **Criação de Notas Musicais:** Suporte a diversas notas, incluindo acordes maiores, menores, sustenidos e oitavas superiores e inferiores.
- **Execução Musical:** Integração com bibliotecas de áudio para tocar músicas em tempo real.
- **Loops:** Repetição de trechos musicais para facilitar composições complexas.
- **Controle de Tempo:** Alteração do tempo (BPM) para ajustar a velocidade da execução.
- **Facilidade de Uso:** Sintaxe clara e intuitiva para iniciantes e avançados.

---

### **Curiosidades**
- A linguagem usa frequências padronizadas para reproduzir notas baseadas na escala temperada.
- Foi projetada para unir aprendizado de programação e música, sendo ideal para quem quer explorar ambas as áreas.
- A linguagem suporta estruturas de repetição, permitindo criar loops que economizam código.

---

### **Gramática (EBNF)**
A linguagem Muh_zica é definida pela seguinte gramática:

```
programa    ::= comando+
comando     ::= "set tempo" NUMERO ";" 
               | "play" NOTA NUMERO ";" 
               | "loop" NUMERO "{" comando+ "}"
NOTA        ::= "Cma" | "Cme" | "Csu" | ... (todas as notas suportadas)
NUMERO      ::= [0-9]+
```

---

### **Exemplos de Uso**
Aqui estão alguns exemplos que mostram como usar a linguagem Muh_zica:

#### 1. **Alterar o tempo e tocar uma sequência:**
```mzc
set tempo 120;
play Ema 4;
play Gma 4;
loop 2 {
    play Fma 4;
    play Ama 4;
}
```

#### 2. **Criar uma melodia simples:**
```mzc
set tempo 100;
play Cma 4;
play Fma 4;
play Gma 4;
```

#### 3. **Usar loops para repetição:**
```mzc
set tempo 140;
loop 3 {
    play Gma 4;
    play Ama 4;
    play Fma 4;
}
```

#### 4. **Composição mais complexa:**
```mzc
set tempo 110;
play Ema 4;
play Fma 4;
play Gma 4;

loop 2 {
    play Ama 4;
    play Gme 4;
    play Fme 4;
}
play Cma 4;
play Gma 4;
play Eme 4;
```

---

### **Como Executar**
1. **Clone o repositório:**
   ```bash
   git clone https://github.com/insper-classroom/24-2-lingpar-linguagem-giovanny_solo.git
   cd 24-2-lingpar-linguagem-giovanny_solo
   ```

2. **Instale as dependências:**
   - Certifique-se de que o Python 3 está instalado.
   - Instale a biblioteca necessária:
     ```bash
     pip install pygame numpy
     ```

3. **Crie ou edite um arquivo `.mzc` com sua música:**
   - Exemplo de arquivo `exemplo.mzc`:
     ```mzc
     set tempo 120;
     play Ema 4;
     play Gma 4;
     ```

4. **Execute o arquivo:**
   ```bash
   python main.py  exemplos/<nome_do_arquivo>
   ```
5. **Exemplo:**
    ```bash
    python main.py exemplos/funk.mzc
    ```
---

### **Estrutura do Projeto**
- **`classes/`**:
  - Contém os componentes principais, como o lexer, parser, e intérprete.
- **`main.py`**:
  - Ponto de entrada para executar a linguagem.
- **`exemplos/`**:
  - Contém exemplos de arquivos `.mzc`.

---

### **Funcionalidades Futuras**
- Suporte a dinâmicas musicais (como forte, piano).
- Exportação para formatos MIDI.
- Integração com bibliotecas gráficas para visualização musical.

---

### **Vídeo**
Assista ao vídeo de apresentação da linguagem para mais detalhes sobre sua criação e funcionamento:
[https://youtu.be/8fWASsHlDC8](#)

