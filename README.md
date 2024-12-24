# Bộ chuẩn hóa địa chỉ Việt Nam (English below)

A package for parsing Vietnamese address

## Cài đặt qua PyPi

```shell
pip3 install vn_address_standardizer
```

## Testing

```python

from VietnameseStandardization import Siameser
std = Siameser.Siameser(stadard_scope='all')
add = '437 Ng. Thì Nhậm P. Kỳ Bá, Thái Bình'
std_add = std.standardize(add)

# output
# {'detail_address': '', 'main_address': {'level1_id': '34', 'level2_id': '336', 'level3_id': '12442', 'name': 'Phường Kỳ Bá', 'type': 'Phường', 'detail': 'Phường Kỳ Bá,Thái Bình,Tỉnh Thái Bình'}, 'similarity_score': 0.6161}

```

---

## [English]

## Features

1. Handling common abbreviations
2. Edit the spelling
3. Correct the order of administrative unit names
4. Add prefix (commune, district, province, ...)

## Install via PyPi

```shell
pip3 install vn_address_standardizer
```

## Testing

```python

from VietnameseStandardization import Siameser
std = Siameser.Siameser(stadard_scope='all')
add = '437 Ng. Thì Nhậm P. Kỳ Bá, Thái Bình'
std_add = std.standardize(add)

# output
# {'detail_address': '', 'main_address': {'level1_id': '34', 'level2_id': '336', 'level3_id': '12442', 'name': 'Phường Kỳ Bá', 'type': 'Phường', 'detail': 'Phường Kỳ Bá,Thái Bình,Tỉnh Thái Bình'}, 'similarity_score': 0.6161}

```
