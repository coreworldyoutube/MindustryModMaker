from flask import Flask, render_template, request
import hjson

app = Flask(__name__)

# フォーム表示
@app.route('/')
def home():
    return render_template('index.html')

# フォーム送信時にMOD設定を生成
@app.route('/generate', methods=['POST'])
def generate():
    # フォームデータの取得
    mod_name = request.form.get('mod_name')
    version = request.form.get('version')
    description = request.form.get('description')
    author = request.form.get('author')
    block_name = request.form.get('block_name')
    block_cost = int(request.form.get('block_cost'))
    
    # MOD設定データ
    mod_data = {
        'name': mod_name,
        'version': version,
        'description': description,
        'author': author,
        'blocks': [
            {
                'name': block_name,
                'buildCost': block_cost
            }
        ]
    }

    # HJSON形式の文字列を生成
    mod_hjson = hjson.dumps(mod_data, indent=2)

    # HJSONをテキストとして表示する
    return render_template('result.html', mod_hjson=mod_hjson)

if __name__ == '__main__':
    app.run(debug=True)
