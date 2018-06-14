"""
Django settings for usda_fns_ingestor project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%*62cyo2f=qeo@fxf1veh8ns@=ea6ft70bqaj+q^end45w3y@_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '.cloud.gov',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'data_ingest',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'usda_fns_ingestor.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'usda_fns_ingestor.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(default='postgres:///usda_fns_ingestor')
}
#    default='postgres+asyncpg:///usda_fns_ingestor')}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

UPLOAD_COLUMNS = [
    'Obs', 'state_ID', '_16_verif_type', '_16_52_verif_no', '_16_SFA_ID',
    '_16_TypeSFA_Public', '_16_TypeSFA_Private', '_16_School_Year_From',
    '_16_School_Year_To', '_16_SFA_Name', '_16_SFA_City', '_16_SFA_Zip_Code',
    '_16_11A_nonrcci_schl', '_16_11B_nonrcci_stud', '_16_12A_rcci_schl',
    '_16_12B_rcci_stud', '_16_12aA_rcci_day_schl', '_16_12aB_rcci_day_stud',
    '_16_12bA_rcci_nonday_schl', '_16_12bB_rcci_nonday_stud',
    '_16_21A_base23_schl', '_16_21B_base23_stud', '_16_22A_nonbase23_schl',
    '_16_22B_nonbase23_stud', '_16_22aB_nonbase23_free_stud',
    '_16_22bB_nonbase23_rp_stud', '_16_23A_cep_schl', '_16_23B_cep_stud',
    '_16_24A_altboth_schl', '_16_24B_altboth_stud', '_16_25A_altoneonly_schl',
    '_16_25B_altoneonly_stud', '_16_31_dc_notrequired', '_16_32B_dc_snap_stud',
    '_16_33B_dc_other_stud', '_16_34B_free_snapletter_stud',
    '_16_41A_free_doc_apps', '_16_41B_free_doc_stud', '_16_42A_free_inc_apps',
    '_16_42B_free_inc_stud', '_16_43A_rp_inc_apps', '_16_43B_rp_inc_stud',
    '_16_t1_tot_free', '_16_t2_tot_rp', '_16_51_exempt',
    '_16_52_verif_yes_before', '_16_52_verif_yes_after',
    '_16_53_verif_type_standard', '_16_53_verif_type_alt1',
    '_16_53_verif_type_alt2', '_16_54_error', '_16_55_selected_apps',
    '_16_56_noverif_sfa', '_16_57A_confirmverf_apps',
    '_16_57B_confirmverf_stud', '_16_58AA_freecat1_r_nc_apps',
    '_16_58AB_freecat1_r_nc_stud', '_16_58AA_freecat2_r_rp_apps',
    '_16_58AB_freecat2_r_rp_stud', '_16_58AA_freecat3_r_paid_apps',
    '_16_58AB_freecat3_r_paid_stud', '_16_58AA_freecat4_n_paid_apps',
    '_16_58AB_freecat4_n_paid_stud', '_16_58BA_freeinc1_r_nc_apps',
    '_16_58BB_freeinc1_r_nc_stud', '_16_58BA_freeinc2_r_rp_apps',
    '_16_58BB_freeinc2_r_rp_stud', '_16_58BA_freeinc3_r_paid_apps',
    '_16_58BB_freeinc3_r_paid_stud', '_16_58BA_freeinc4_n_paid_apps',
    '_16_58BB_freeinc4_n_paid_stud', '_16_58CA_rp1_r_nc_apps',
    '_16_58CB_rp1_r_nc_stud', '_16_58CA_rp2_r_free_apps',
    '_16_58CB_rp2_r_free_stud', '_16_58CA_rp3_r_paid_apps',
    '_16_58CB_rp3_r_paid_stud', '_16_58CA_rp4_n_paid_apps',
    '_16_58CB_rp4_n_paid_stud', '_16_vc1_forcause',
    '_16_calculated_verif_sample', '_16_SFAs', '_16_enrollment',
    '_16_total_schls', '_16_enr_avg', '_16_provision_schls',
    '_16_provision_stud', '_16_direct_cert_stud', '_16_apps_approved',
    '_16_stud_approved', '_16_FREERPtoENR', '_16_FREEcatel_studTOapps',
    '_16_FREEinc_studTOapps', '_16_RPinc_studTOapps', '_16_contacted_apps',
    '_16_contacted_stud', '_16_responded_stud', '_16_noresponse_stud',
    '_16_r_nc_stud', '_16_r_chg_stud', '_16_responded_apps',
    '_16_noresponse_apps', '_16_r_nc_apps', '_16_r_chg_apps',
    '_16_completed_verif', '_16_enrclass', '_16_std_verif_sample',
    '_16_alt1_verif_sample', '_16_alt2_verif_sample', '_16_confirmrate',
    '_16_NRrate', '_16_Rrate', '_16_contacted_and_dv', '_16_DirectVerRate',
    '_16_TradVerRate', '_16_742_errors', '_16_atleastone742error',
    '_16_742_errorSUM', '_16_check1', '_16_check2', '_16_check3', '_16_check4',
    '_16_check5', '_16_check6', '_16_check7', '_16_check8', '_16_check9',
    '_16_check10', '_16_check11', '_16_check12', '_16_check13W',
    '_16_check14W', '_16_check15W', '_16_check16W', '_16_check17',
    '_16_check18', '_16_check19', '_16_check20', '_16_check21', '_16_check22',
    '_16_check23', '_16_check24', '_16_check25', '_16_check26', '_16_check27',
    '_16_check28', '_16_check29', '_16_check30', '_16_check31', '_16_check32',
    '_16_check33', '_16_check34', '_16_check35W', '_16_check36W',
    '_16_check37W', '_16_check38', '_16_check39', '_16_check40W',
    '_16_check41W', '_16_check42W', '_16_check43W', '_16_check44W',
    '_16_check45', '_16_check46', '_16_check47W', '_16_check48W',
    '_16_check49W', '_16_check50W', '_16_check51', '_16_check52W',
    '_16_check53W', '_16_check54W', '_16_check55W', '_16_check56W',
    '_16_check57W', '_16_check58', '_16_check59W', '_16_check60',
    '_16_check61W', '_16_check62', '_16_check63W', '_16_check64',
    '_16_check65W', '_16_check66', '_16_check67W', '_16_check68',
    '_16_check69W', '_16_check70', '_16_check71', '_16_check72W',
    '_16_check73', '_16_check74', '_16_check75W', '_16_check76', '_16_check77',
    '_16_check78W', '_16_check79', '_16_check80', '_16_check81',
    '_16_check82W', '_16_check83W', '_16_check84', '_16_check85',
    '_16_check86', '_16_check87', '_16_check88', '_16_check89', '_16_check90',
    '_16_check91', '_16_check92', '_16_check93', '_16_check94', '_16_check95',
    '_16_check96', '_16_check97', '_16_check98', '_16_check99', '_16_check100',
    '_16_check101', '_16_check102', '_16_check103', '_16_check104',
    '_16_check105', '_16_check106W', '_16_check107', '_16_check108',
    '_16_check109', '_16_check110W', '_16_check111W', '_16_check112W',
    '_16_check113W', '_16_check114', '_16_check115', '_16_check116',
    '_16_check117W', '_16_check118', '_16_check119', '_16_check120W',
    '_16_check121W', '_16_check122W', '_16_check123W', '_16_check124'
]

DATA_INGEST = {
    'VALIDATORS': {
        # 'usda_fns.json': 'data_ingest.ingestors.GoodtablesValidator',
        'usda_sql_rules.yml': 'data_ingest.ingestors.SqlValidatorFailureConditions',
    },
    'STREAM_ARGS': {
        'sheet': 'Data',  # Uses the 'Data' sheet from workbook if .xlsx
        'headers': UPLOAD_COLUMNS,
    },
    'OLD_HEADER_ROW': 1,
}