def generate_book_cat_count_list(cat_cnts):
    result = ""
    for cat_cnt in cat_cnts:
        result += f"<li>{cat_cnt['category']}: {cat_cnt['cnt']}"
    return result