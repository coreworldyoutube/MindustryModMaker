from flask import Flask, render_template, request, send_file
import hjson
import os

app = Flask(__name__)

# フォーム表示
@app.route('/')
def home():
    return render_template('index.html')

# フォーム送信時にMODファイルを生成
@app.route('/generate', methods=['POST'])
def generate():
    # フォームデータの取得
    mod_name = request.form.get('mod_name')
    version = request.form.get('version')
    description = request.form.get('description')
    author = request.form.get('author')
    block_name = request.form.get('block_name')
    block_health = int(request.form.get('block_health'))
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
                'health': block_health,
                'buildCost': block_cost
            }
        ]
    }

    # HJSONファイルの生成
    file_path = 'mod.hjson'
    with open(file_path, 'w') as file:
        hjson.dump(mod_data, file, indent=2)

    # 生成したHJSONファイルをダウンロードできるように
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
