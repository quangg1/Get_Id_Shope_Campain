import streamlit as st
import json

# Nhập dữ liệu JSON trực tiếp
json_input = st.text_area("Dán dữ liệu JSON sản phẩm (dạng raw)")

# Nhập danh sách sản phẩm
product_input = st.text_area("Nhập danh sách sản phẩm (mỗi dòng một sản phẩm)")

if json_input and product_input:
    try:
        # Đọc dữ liệu JSON từ input
        data = json.loads(json_input)

        # Tách danh sách sản phẩm
        product_list = [p.strip().lower() for p in product_input.split('\n') if p.strip()]

        # So sánh
        matched_products = []
        for item in data['data']['items']:
            item_name = item['name'].strip().lower()
            for product in product_list:
                if product == item_name:
                    matched_products.append({
                        "Tên sản phẩm": item['name'],
                        "ID": item['item_id']
                    })

        # Hiển thị kết quả
        if matched_products:
            st.success(f"Tìm thấy {len(matched_products)} sản phẩm trùng khớp:")
            st.table(matched_products)
        else:
            st.warning("Không tìm thấy sản phẩm nào trùng khớp.")
    except json.JSONDecodeError:
        st.error("Dữ liệu JSON không hợp lệ. Vui lòng kiểm tra lại.")
