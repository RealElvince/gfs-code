def code_generator(group_name, county_code, constituency_code, group_nature, group_activity, group_number):
    fund_code = "4"
    domestic_code = 411000 + group_nature
    activity_code = group_activity + group_nature

    gfs_code = f"{fund_code}-{county_code:03d}-{constituency_code:03d}-{domestic_code}-{activity_code}-{group_number:03d}"
    print(f"GFS CODE for {group_name} is: {gfs_code}")