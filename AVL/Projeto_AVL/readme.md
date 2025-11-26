# Visualizador de Árvore AVL Interativo

Este projeto é uma aplicação web desenvolvida em **Python** com **Flask** que implementa uma **Árvore AVL** (Adelson-Velsky e Landis). O objetivo é fornecer uma interface visual limpa e interativa para demonstrar as operações de inserção, remoção e o balanceamento automático da árvore.

### Funcionalidades
* **Adicionar Nós:** Insere valores inteiros na árvore.
* **Remover Nós:** Remove valores e reestrutura a árvore automaticamente.
* **Balanceamento Automático:** A árvore se ajusta após cada operação para manter a propriedade AVL.
* **Visualização Gráfica:** Uso da biblioteca **Vis.js** para renderizar a árvore dinamicamente.
* **Indicadores Visuais:** Exibição do valor do nó e seu **Fator de Balanceamento (FB)**.

## 📂 Estrutura de Arquivos

```text
/
├── app.py              # Código fonte principal (Flask + Lógica AVL)
├── DOCUMENTATION.md    # Explicação detalhada da lógica e matemática da AVL
├── README.md           # Instruções de instalação e uso
└── templates/
    └── index.html      # Frontend (HTML/CSS/JS com Vis.js)
```

3. Instalar Dependências
pip install flask

4. Executar a Aplicação
python app.py

5. Acessar
Abra o seu navegador e acesse o endereço indicado no terminal (geralmente):

https://www.google.com/search?q=http://127.0.0.1:5000

🛠️ Tecnologias Utilizadas

Backend: Python, Flask

Frontend: HTML5, CSS3, JavaScript