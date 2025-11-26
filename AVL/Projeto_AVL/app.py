from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1


class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def adicionar(self, valor):
        self.raiz = self._adicionar_no(self.raiz, valor)

    def _adicionar_no(self, no, valor):
        if not no:
            return No(valor)
        elif valor < no.valor:
            no.esquerda = self._adicionar_no(no.esquerda, valor)
        else:
            no.direita = self._adicionar_no(no.direita, valor)

        no.altura = 1 + max(self._get_altura(no.esquerda), self._get_altura(no.direita))
        return self._balancear(no)

    def remover(self, valor):
        self.raiz = self._remover_no(self.raiz, valor)

    def _remover_no(self, no, valor):
        if not no:
            return no
        elif valor < no.valor:
            no.esquerda = self._remover_no(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self._remover_no(no.direita, valor)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda
            temp = self._get_minimo(no.direita)
            no.valor = temp.valor
            no.direita = self._remover_no(no.direita, temp.valor)

        no.altura = 1 + max(self._get_altura(no.esquerda), self._get_altura(no.direita))
        return self._balancear(no)

    def _get_altura(self, no):
        if not no:
            return 0
        return no.altura

    def _get_balanceamento(self, no):
        if not no:
            return 0
        return self._get_altura(no.direita) - self._get_altura(no.esquerda)

    def _get_minimo(self, no):
        if no is None or no.esquerda is None:
            return no
        return self._get_minimo(no.esquerda)

    def _balancear(self, no):
        fb = self._get_balanceamento(no)

        if fb < -1:
            if self._get_balanceamento(no.esquerda) > 0:
                no.esquerda = self._rotacao_esquerda(no.esquerda)
            return self._rotacao_direita(no)

        if fb > 1:
            if self._get_balanceamento(no.direita) < 0:
                no.direita = self._rotacao_direita(no.direita)
            return self._rotacao_esquerda(no)

        return no

    def _rotacao_esquerda(self, z):
        y = z.direita
        T2 = y.esquerda
        y.esquerda = z
        z.direita = T2
        z.altura = 1 + max(self._get_altura(z.esquerda), self._get_altura(z.direita))
        y.altura = 1 + max(self._get_altura(y.esquerda), self._get_altura(y.direita))
        return y

    def _rotacao_direita(self, z):
        y = z.esquerda
        T3 = y.direita
        y.direita = z
        z.esquerda = T3
        z.altura = 1 + max(self._get_altura(z.esquerda), self._get_altura(z.direita))
        y.altura = 1 + max(self._get_altura(y.esquerda), self._get_altura(y.direita))
        return y

    def para_dict(self):
        nos = []
        arestas = []
        self._construir_dados_visualizacao(self.raiz, nos, arestas)
        return {"nodes": nos, "edges": arestas}

    def _construir_dados_visualizacao(self, no, nos, arestas):
        if no:
            fb = self._get_balanceamento(no)
            label_visual = f"{no.valor}\n(FB: {fb})"

            nos.append({
                "id": no.valor,
                "label": label_visual,
                "title": f"Valor: {no.valor}, Altura: {no.altura}, FB: {fb}"
            })

            if no.esquerda:
                arestas.append({"from": no.valor, "to": no.esquerda.valor})
                self._construir_dados_visualizacao(no.esquerda, nos, arestas)
            if no.direita:
                arestas.append({"from": no.valor, "to": no.direita.valor})
                self._construir_dados_visualizacao(no.direita, nos, arestas)


avl = ArvoreAVL()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/arvore', methods=['GET'])
def get_arvore():
    return jsonify(avl.para_dict())


@app.route('/api/adicionar', methods=['POST'])
def adicionar():
    data = request.json
    try:
        valor = int(data.get('valor'))
        avl.adicionar(valor)
        return jsonify({"status": "sucesso", "mensagem": f"Valor {valor} adicionado"})
    except (ValueError, TypeError):
        return jsonify({"status": "erro", "mensagem": "Valor inválido"}), 400


@app.route('/api/remover', methods=['POST'])
def remover():
    data = request.json
    try:
        valor = int(data.get('valor'))
        avl.remover(valor)
        return jsonify({"status": "sucesso", "mensagem": f"Valor {valor} removido"})
    except (ValueError, TypeError):
        return jsonify({"status": "erro", "mensagem": "Valor inválido"}), 400


if __name__ == '__main__':
    app.run(debug=True)