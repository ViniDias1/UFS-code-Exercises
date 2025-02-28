import random
import dump
import modelo

def classifica_issues_dump(issues):

    total_issues_count = 0
    all_issues = []
    for issue in issues:

        title = issue.get("title", "Sem título")  
        body = issue.get("body", "Sem descrição")  

        resultado = modelo.issue_classification(title, body)

        if resultado:
            print(f"A issue foi classificada como: {resultado}")
            issue.update({"Resultado": f'{resultado}'})
            all_issues.append(issue)
            total_issues_count += 1
        else:
            print("A issue não foi aprovada para ser salva no banco de dados.")

    return [all_issues,total_issues_count]

def main():

    dump.create_db()

    total_issues = 200
    per_page = 10
    page = 1
    total_issues_count = 0
    #pages = total_issues // per_page
    all_issues = []

    while True:

        issues = (dump.fetch_issues(page, per_page))
        
        resultado = classifica_issues_dump(issues)
        
        all_issues.extend(resultado[0])
        total_issues_count += resultado[1]

        if total_issues_count >= total_issues:
            break
        
        page -= 10

    dump.save_issues_to_db(all_issues)
    print(f"{total_issues_count} issues salvas no banco de dados!")


if __name__ == "__main__":
    main()